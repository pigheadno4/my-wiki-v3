---
title: "PayPal 单选按钮支付墙：PayPal + 分期付款（非美国商户，面向美国买家）"
type: analysis
date_created: 2026-04-16
tags:
  [
    paypal,
    pay-later,
    radio-button,
    payment-wall,
    funding-eligibility,
    marks,
    standalone-buttons,
    js-sdk,
    bnpl,
    messaging,
    cross-border,
    us,
  ]
---

## 概述

单选按钮支付墙允许买家在点击支付按钮前先选择付款方式。本指南介绍如何为**非美国商户账户、面向美国买家**的场景，将 **PayPal** 和 **分期付款（Pay Later）** 整合为两个独立的单选项，包含：

- 分期付款消息显示在**单选标签旁边**（选择前），提前展示优惠
- 分期付款消息显示在**按钮下方**（选择后），使用 `contextualComponents: 'PAY_LATER_BUTTON'`
- 分期付款按钮设为**蓝色**，与 PayPal 按钮（金色）形成视觉区分
- PayLater验证，确保不可用的选项不会显示

**适用范围：** 非美国商户账户，面向美国买家，使用美元（USD）。需要 PayPal 审批跨境消息功能（限量开放）— 上线前请联系 PayPal 客户经理。审批流程详见 [[analysis-paypal-pay-later-fr-integration-guide]]。

> **与美国商户集成的关键区别：** 由于商户账户非美国账户，`data-pp-buyercountry="US"` 必须添加到**每一个** `data-pp-message` 元素上，且 SDK URL 中必须包含 `enable-funding=paylater`。缺少这两项，分期付款消息将无法渲染，分期付款按钮也可能无法显示。

## 前提条件

- 非美国 PayPal 商业账户，并已完成基础 Checkout 集成
- PayPal 跨境消息功能审批（限量开放）
- Orders REST API 集成

## SDK 脚本标签

一个 `<script>` 标签即可。`enable-funding=paylater` 对非美国商户账户**必填** — 缺少则分期付款按钮不会渲染。`marks` 提供单选标签旁的支付方式图标。`funding-eligibility` 用于启用 `isEligible()`：

```html
<script src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&components=messages,buttons,funding-eligibility,marks&currency=USD&enable-funding=paylater"></script>
```

## HTML 结构

每个支付方式行**默认隐藏**，仅在确认资格后才显示。分期付款有两处消息：一处在单选标签区域（行显示时始终可见），一处在按钮面板内（选择后显示）。两处均携带 `data-pp-buyercountry="US"`。

```html
<!-- ── PayPal 行 ──────────────────────────────────────────────── -->
<div id="row-paypal" class="payment-row" style="display: none;">
  <label>
    <input type="radio" name="payment-method" value="paypal" />
    <span id="mark-paypal"></span>
    <!-- PayPal 图标渲染位置 -->
    <span>PayPal</span>
  </label>
  <!-- 按钮面板：选中单选后才显示 -->
  <div id="panel-paypal" class="payment-panel" style="display: none;">
    <div id="button-paypal"></div>
  </div>
</div>

<!-- ── 分期付款行 ──────────────────────────────────────────── -->
<div id="row-paylater" class="payment-row" style="display: none;">
  <label>
    <input type="radio" name="payment-method" value="paylater" />
    <span id="mark-paylater"></span>
    <!-- 分期付款图标渲染位置 -->
    <span>分期付款</span>
    <!-- 单选标签旁的消息 — 在选择前展示优惠 -->
    <div
      data-pp-message
      data-pp-placement="payment"
      data-pp-amount="150.00"
      data-pp-buyercountry="US"
      data-pp-style-layout="text"
      data-pp-style-logo-type="none"
      data-pp-style-text-color="black"
      data-pp-style-text-size="12"
    ></div>
  </label>
  <!-- 按钮面板：选中单选后才显示 -->
  <div id="panel-paylater" class="payment-panel" style="display: none;">
    <div id="button-paylater"></div>
    <!-- 按钮下方消息，与 PAY_LATER_BUTTON 上下文协调 -->
    <div
      data-pp-message
      data-pp-placement="payment"
      data-pp-amount="150.00"
      data-pp-buyercountry="US"
      data-pp-contextualcomponents="PAY_LATER_BUTTON"
    ></div>
  </div>
</div>
```

> **为什么需要两处消息？**
>
> - **单选标签旁消息**（`logo-type: none`）— 在买家选择分期付款前显示"4 期免息，每期 $X"，帮助买家提前了解优惠，不会造成标签拥挤。
> - **面板内消息**（`contextualComponents: PAY_LATER_BUTTON`）— 选择后在按钮下方显示分期消息，与蓝色分期按钮形成视觉协调。`PAY_LATER_BUTTON` 会隐藏 logo，因为按钮本身已携带品牌标识。

## JavaScript — 资格验证与渲染

```javascript
// ── 公共订单逻辑 ──────────────────────────────────────────────────────────
function createOrder(data, actions) {
  return actions.order.create({
    purchase_units: [
      {
        amount: {
          currency_code: "USD",
          value: "150.00", // 请替换为实际购物车金额
        },
      },
    ],
  });
}

function onApprove(data, actions) {
  return actions.order.capture().then(function (details) {
    console.log("订单已捕获：", details);
    // 跳转至确认页
  });
}

function onError(err) {
  console.error("PayPal 错误：", err);
}

// ── 辅助函数：绑定单选切换以显示/隐藏面板 ───────────────────────────────
function bindRadioToggle(value, panelId) {
  document
    .querySelectorAll('input[name="payment-method"]')
    .forEach(function (radio) {
      radio.addEventListener("change", function () {
        // 折叠所有面板
        document.querySelectorAll(".payment-panel").forEach(function (panel) {
          panel.style.display = "none";
        });
        // 展开选中方式的面板
        if (this.value === value) {
          document.getElementById(panelId).style.display = "block";
        }
      });
    });
}

// ── PayPal 按钮（金色 — 默认） ────────────────────────────────────────────
(function () {
  var paypalButton = paypal.Buttons({
    fundingSource: paypal.FUNDING.PAYPAL,
    style: {
      color: "gold", // 默认值，显式声明便于阅读
      shape: "rect",
      layout: "vertical",
    },
    createOrder: createOrder,
    onApprove: onApprove,
    onError: onError,
  });

  if (paypalButton.isEligible()) {
    document.getElementById("row-paypal").style.display = "block";
    paypal
      .Marks({ fundingSource: paypal.FUNDING.PAYPAL })
      .render("#mark-paypal");
    paypalButton.render("#button-paypal");
    bindRadioToggle("paypal", "panel-paypal");
  }
  // 不符合资格 → 行保持隐藏，选项永远不显示
})();

// ── 分期付款按钮（蓝色 — 与 PayPal 金色区分） ────────────────────────────
(function () {
  var payLaterButton = paypal.Buttons({
    fundingSource: paypal.FUNDING.PAYLATER,
    style: {
      color: "blue", // 与 PayPal 金色按钮形成区分
      shape: "rect",
      layout: "vertical",
    },
    createOrder: createOrder,
    onApprove: onApprove,
    onError: onError,
  });

  if (payLaterButton.isEligible()) {
    document.getElementById("row-paylater").style.display = "block";
    paypal
      .Marks({ fundingSource: paypal.FUNDING.PAYLATER })
      .render("#mark-paylater");
    payLaterButton.render("#button-paylater");
    bindRadioToggle("paylater", "panel-paylater");
  }
  // 不符合资格 → 行保持隐藏，选项永远不显示
})();

// ── 预选第一个符合资格的行 ────────────────────────────────────────────────
var firstRadio = document.querySelector(
  '.payment-row:not([style*="display: none"]) input[type="radio"]',
);
if (firstRadio) {
  firstRadio.checked = true;
  firstRadio.dispatchEvent(new Event("change"));
}
```

## React 集成（`@paypal/react-paypal-js`）

安装依赖包：

```bash
npm install @paypal/react-paypal-js
```

### 核心组件说明

| 组件                     | 用途                                                                |
| ------------------------ | ------------------------------------------------------------------- |
| `<PayPalScriptProvider>` | 在应用根节点加载一次 SDK，替代 `<script>` 标签                      |
| `<PayPalButtons>`        | 渲染指定 `fundingSource` 的支付按钮，内部调用 `isEligible()`        |
| `<PayPalMarks>`          | 渲染支付方式图标                                                    |
| `<PayPalMessages>`       | 渲染分期付款消息                                                    |
| `usePayPalScriptReducer` | 读取 SDK 加载状态的 Hook（`isPending`、`isResolved`、`isRejected`） |
| `FUNDING`                | 导出的常量 — `FUNDING.PAYPAL`、`FUNDING.PAYLATER`                   |

### Provider 配置

`PayPalScriptProvider` 接受所有 SDK URL 参数的驼峰命名版本。请放在应用根节点，不要放在结账组件内部：

```jsx
import { PayPalScriptProvider } from "@paypal/react-paypal-js";

const PAYPAL_OPTIONS = {
  clientId: "YOUR_CLIENT_ID",
  buyerCountry: "US", // 仅限沙箱环境 — 生产环境请删除
  currency: "USD",
  components: "messages,buttons,funding-eligibility,marks",
  enableFunding: "paylater", // 非美国商户账户必填
};

export default function App() {
  return (
    <PayPalScriptProvider options={PAYPAL_OPTIONS}>
      <CheckoutPage />
    </PayPalScriptProvider>
  );
}
```

### 资格验证处理

`<PayPalButtons>` 内部调用 `isEligible()`。不符合资格时渲染 `children` prop 而非按钮 — 利用此机制检测资格并隐藏单选行：

```jsx
import {
  PayPalButtons,
  PayPalMarks,
  PayPalMessages,
  FUNDING,
  usePayPalScriptReducer,
} from "@paypal/react-paypal-js";

function PaymentWall() {
  const [{ isResolved }] = usePayPalScriptReducer();
  const [selected, setSelected] = useState(null);
  const [paypalEligible, setPaypalEligible] = useState(null); // null = 未知
  const [payLaterEligible, setPayLaterEligible] = useState(null);

  // 两者资格确认后，预选第一个符合条件的选项
  useEffect(() => {
    if (paypalEligible === null || payLaterEligible === null) return;
    if (selected !== null) return;
    if (paypalEligible) setSelected("paypal");
    else if (payLaterEligible) setSelected("paylater");
  }, [paypalEligible, payLaterEligible, selected]);

  if (!isResolved) return <p>正在检查可用支付方式…</p>;

  return (
    <div className="payment-wall">
      {/* ── PayPal 行 ── */}
      {/* 隐藏探针 — 仅检测资格，不显示按钮 */}
      <div style={{ display: "none" }}>
        <PayPalButtons
          fundingSource={FUNDING.PAYPAL}
          onInit={() => setPaypalEligible(true)}
          createOrder={createOrder}
          onApprove={onApprove}
          onError={onError}
        >
          {/* 不符合资格时渲染 children */}
          <IneligibleSignal onIneligible={() => setPaypalEligible(false)} />
        </PayPalButtons>
      </div>

      {paypalEligible && (
        <div className="payment-row">
          <label>
            <input
              type="radio"
              name="payment-method"
              value="paypal"
              checked={selected === "paypal"}
              onChange={() => setSelected("paypal")}
            />
            <PayPalMarks fundingSource={FUNDING.PAYPAL} />
            <span>PayPal</span>
          </label>
          {selected === "paypal" && (
            <div className="panel">
              <PayPalButtons
                fundingSource={FUNDING.PAYPAL}
                style={{ color: "gold", shape: "rect", layout: "vertical" }}
                createOrder={createOrder}
                onApprove={onApprove}
                onError={onError}
              />
            </div>
          )}
        </div>
      )}

      {/* ── 分期付款行 ── */}
      <div style={{ display: "none" }}>
        <PayPalButtons
          fundingSource={FUNDING.PAYLATER}
          onInit={() => setPayLaterEligible(true)}
          createOrder={createOrder}
          onApprove={onApprove}
          onError={onError}
        >
          <IneligibleSignal onIneligible={() => setPayLaterEligible(false)} />
        </PayPalButtons>
      </div>

      {payLaterEligible && (
        <div className="payment-row">
          <label>
            <input
              type="radio"
              name="payment-method"
              value="paylater"
              checked={selected === "paylater"}
              onChange={() => setSelected("paylater")}
            />
            <PayPalMarks fundingSource={FUNDING.PAYLATER} />
            <span>分期付款</span>
            {/* 单选标签旁的消息 */}
            <PayPalMessages
              style={{
                layout: "text",
                logo: { type: "none" },
                text: { color: "black", size: 12 },
              }}
              amount={150.0}
              placement="payment"
              buyerCountry="US"
            />
          </label>
          {selected === "paylater" && (
            <div className="panel">
              <PayPalButtons
                fundingSource={FUNDING.PAYLATER}
                style={{ color: "blue", shape: "rect", layout: "vertical" }}
                createOrder={createOrder}
                onApprove={onApprove}
                onError={onError}
              />
              {/* 按钮下方消息 */}
              <PayPalMessages
                amount={150.0}
                placement="payment"
                buyerCountry="US"
                contextualComponents="PAY_LATER_BUTTON"
              />
            </div>
          )}
        </div>
      )}
    </div>
  );
}

// 在 PayPalButtons 不符合资格时渲染 — 触发回调后返回 null
function IneligibleSignal({ onIneligible }) {
  const called = useRef(false);
  useEffect(() => {
    if (!called.current) {
      called.current = true;
      onIneligible();
    }
  }, [onIneligible]);
  return null;
}
```

### React 特有注意事项

| 主题                            | 说明                                                                                                       |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| SDK URL 参数                    | `options` 中使用驼峰命名：`clientId`、`enableFunding`、`buyerCountry` — Provider 会自动转换为 URL 查询参数 |
| `buyerCountry`                  | 与原生 JS 相同的跨境要求 — 在 `PAYPAL_OPTIONS` 和每个 `<PayPalMessages>` 组件上都需要传入                  |
| 资格探针                        | `<PayPalButtons>` 不直接暴露 `isEligible()` — 使用隐藏探针 + `children` 不符合资格回退来检测               |
| `onInit`                        | 按钮成功初始化（即符合资格）时触发 — 与 `children` 回退配合使用来设置资格状态                              |
| `forceReRender`                 | 订单金额动态变化时，向 `<PayPalButtons>` 传入 `forceReRender={[amount]}` — 触发按钮完整重渲染              |
| `usePayPalScriptReducer`        | 使用 `isResolved` 控制渲染时机 — 避免 SDK 加载完成前闪现"无可用选项"                                       |
| 不要嵌套 `PayPalScriptProvider` | 只放在应用根节点一次，不要放在支付墙组件内部                                                               |

## 消息位置汇总

| 位置         | `data-pp-` 配置                                              | 可见时机                                   |
| ------------ | ------------------------------------------------------------ | ------------------------------------------ |
| 单选标签旁   | `buyercountry: US`，`logo-type: none`，`placement: payment`  | 分期付款行符合资格时（行显示期间始终可见） |
| 分期按钮下方 | `buyercountry: US`，`contextualComponents: PAY_LATER_BUTTON` | 买家选中分期付款单选                       |

## 资格验证流程

```text
SDK 加载（包含 enable-funding=paylater）
    │
    ├─ PAYPAL.isEligible()?
    │       是 → 显示行，渲染金色图标 + 金色按钮
    │       否 → 行保持隐藏
    │
    └─ PAYLATER.isEligible()?
            是 → 显示行，渲染分期图标 + 蓝色按钮 + 标签消息
            否 → 行保持隐藏

买家选中单选
    └─ 折叠所有面板 → 展开选中方式的面板
            选中 PAYPAL   → 显示金色按钮
            选中 PAYLATER → 显示蓝色按钮 + 面板消息（PAY_LATER_BUTTON）
```

## 按钮颜色参考

| 按钮     | `style.color`  | 原因                                                |
| -------- | -------------- | --------------------------------------------------- |
| PayPal   | `gold`（默认） | PayPal 推荐颜色，识别度和转化率最高                 |
| 分期付款 | `blue`         | PayPal 第一备选颜色，与金色形成区分，仍符合品牌规范 |

有效颜色值：`gold`、`blue`、`silver`、`white`、`black`。

## 为什么 `isEligible()` 是正确的验证方式

| 机制                                   | 作用                                             | 是否足够                      |
| -------------------------------------- | ------------------------------------------------ | ----------------------------- |
| SDK URL 中的 `enable-funding=paylater` | 告知 SDK 尝试为非美国商户加载分期付款            | 否 — 允许资格检查，不保证通过 |
| `paypal.Buttons(...).isEligible()`     | 运行时按会话检查：该买家/金额/账户是否符合条件？ | 是 — 最终的资格判断           |

渲染前务必调用 `isEligible()`。永远不要为可能无法渲染的按钮显示单选行。

## 关键规则

| 规则                            | 说明                                                                                         |
| ------------------------------- | -------------------------------------------------------------------------------------------- |
| 需要 PayPal 审批                | 跨境消息为**限量开放** — 上线前必须获得审批                                                  |
| `enable-funding=paylater`       | 非美国商户账户**必填** — 缺少则分期付款按钮不会渲染                                          |
| `data-pp-buyercountry="US"`     | 每个 `data-pp-message` 元素上**必填** — 非美国商户缺少此项则消息不渲染                       |
| `funding-eligibility` 组件      | `components=` 中必须包含，`isEligible()` 才能正常工作                                        |
| `marks` 组件                    | `components=` 中必须包含，`paypal.Marks()` 才能使用                                          |
| `messages` 组件                 | `components=` 中必须包含，`data-pp-message` 元素才能渲染                                     |
| 对单选行进行资格验证            | 永远不要为无法渲染的按钮显示单选选项                                                         |
| 每页只加载一次 SDK              | 所有组件合并到单个 `<script>` 标签                                                           |
| `Buttons()` 内的 `message` 选项 | **仅限美国商户 + 美国买家** — 本场景不适用；请改用带 `buyercountry` 的独立 `data-pp-message` |
| 禁止修改消息内容                | 不得翻译、调整大小、改变颜色或以任何方式修改分期付款消息文本                                 |
| 动态更新金额                    | 直接设置 `data-pp-amount` 属性，SDK 自动重渲染 — 不要再次调用 `render()`                     |

## 相关 Wiki 页面

- [[paypal-checkout]] — 基础 Checkout 集成
- [[paypal-pay-later]] — 各国分期付款产品详情
- [[analysis-paypal-pay-later-fr-integration-guide]] — 跨境消息审批流程及法国场景示例

## 来源

- [[source-paypal-checkout-standalone-buttons]] — `isEligible()`、`paypal.FUNDING.*`、单选按钮 + Marks 模式、`enable-funding`；已通过沙箱 Demo 验证 `paypal.Marks({ fundingSource: paypal.FUNDING.PAYLATER })` 可渲染分期付款图标
- [[source-paypal-checkout-display-payment-methods]] — 单选按钮支付墙结构，显示/隐藏切换逻辑
- [[source-paypal-checkout-display-funding-source]] — `fundingSource` 取值及分期付款本地化表格
- [[source-paypal-pay-later]] — 分期付款消息、`data-pp-*` 属性、`contextualComponents` 取值、跨境 `buyerCountry`
- [[source-paypal-checkout-messaging-with-buttons]] — 确认 `Buttons()` 内 `message` 选项仅限美国场景
- [[source-paypal-react-paypal-js-readme]] — `@paypal/react-paypal-js`：`PayPalScriptProvider`、`PayPalButtons`、`PayPalMarks`、`PayPalMessages`、`usePayPalScriptReducer`、`FUNDING` 常量
