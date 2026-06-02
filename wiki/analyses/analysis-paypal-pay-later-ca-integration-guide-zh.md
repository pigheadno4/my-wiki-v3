---
title: "PayPal 加拿大分期付款按钮与消息集成指南（加拿大商户）"
type: analysis
date_created: 2026-04-16
tags: [paypal, pay-later, canada, ca, messaging, button, js-sdk, enable-funding, bnpl, bilingual, french, english]
---

## 概述

面向**加拿大 PayPal 商户**的分期付款按钮与消息集成分步指南。

**加拿大分期付款产品：**

| 产品 | 期数 | 还款周期 | 金额范围 |
| --- | --- | --- | --- |
| Pay in 4（4 期付款） | 4 期 | 首期在结账时支付，后续每 2 周一期（双周） | CAD $30–$1,500 |

**加拿大特有要求：** 加拿大要求支持**双语** — 英语（`en_CA`）和法语（`fr_CA`）。SDK URL 中的 `locale` 参数控制按钮语言；`data-pp-language` 控制消息语言。必须根据买家所在的站点语言提供对应版本。

## 前提条件

- 加拿大 PayPal 商业账户
- 面向加拿大市场、以加拿大元（CAD）结算的网站
- 一次性付款集成（循环付款/参考交易不符合资格）
- 已完成 PayPal Checkout 基础集成

## SDK 脚本标签

`enable-funding=paylater` **必填** — 缺少则加拿大商户的分期付款按钮不会渲染。`locale` 需与页面语言匹配：

**英语站点：**

```html
<script
  src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&components=messages,buttons,funding-eligibility,marks&currency=CAD&enable-funding=paylater&locale=en_CA"
></script>
```

**法语站点：**

```html
<script
  src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&components=messages,buttons,funding-eligibility,marks&currency=CAD&enable-funding=paylater&locale=fr_CA"
></script>
```

> 每个页面只加载一次 `<script>` 标签。如果站点需要动态切换语言（SPA），通过 `usePayPalScriptReducer` 的 `resetOptions`（React）或刷新页面并更新 URL 参数来重新加载 SDK。

## 分期付款消息

在每个 `data-pp-message` 元素上添加 `data-pp-language` 以匹配页面语言。无需 `data-pp-buyercountry` — 加拿大商户账户会自动解析加拿大资格。

**英语消息：**

```html
<div
  data-pp-message
  data-pp-placement="product"
  data-pp-amount="150.00"
  data-pp-language="en-CA"
  data-pp-style-layout="text"
  data-pp-style-logo-type="inline"
  data-pp-style-text-color="black"
  data-pp-style-text-size="12"
></div>
```

**法语消息：**

```html
<div
  data-pp-message
  data-pp-placement="product"
  data-pp-amount="150.00"
  data-pp-language="fr-CA"
  data-pp-style-layout="text"
  data-pp-style-logo-type="inline"
  data-pp-style-text-color="black"
  data-pp-style-text-size="12"
></div>
```

### 消息放置位置

| 页面位置 | `data-pp-placement` 值 |
| --- | --- |
| 商品页 | `product` |
| 购物车页 | `cart` |
| 结账页 | `payment` |
| 首页 | `home` |
| 分类页 | `category` |

### 动态更新金额

SDK 自动监听 `data-pp-amount` 属性变化并重新渲染 — **不要**再次调用 `render()`：

```javascript
document.querySelector('[data-pp-message]')
  .setAttribute('data-pp-amount', newAmount);
```

## 分期付款按钮

`en_CA` 语言环境下按钮渲染为 **"Pay in 4"**，`fr_CA` 下渲染为 **"Payez en 4 fois"**。务必通过 `isEligible()` 验证资格。

```html
<div id="paylater-button-container"></div>
```

```javascript
var payLaterButton = paypal.Buttons({
  fundingSource: paypal.FUNDING.PAYLATER,
  style: {
    color: 'gold',    // 或使用 'blue' 与 PayPal 按钮形成区分
    shape: 'rect',
    layout: 'vertical',
  },
  createOrder: function(data, actions) {
    return actions.order.create({
      purchase_units: [{
        amount: {
          currency_code: 'CAD',
          value: '150.00'  // 请替换为实际购物车金额
        }
      }]
    });
  },
  onApprove: function(data, actions) {
    return actions.order.capture().then(function(details) {
      console.log('订单已捕获：', details);
    });
  },
  onError: function(err) {
    console.error('PayPal 错误：', err);
  }
});

if (payLaterButton.isEligible()) {
  payLaterButton.render('#paylater-button-container');
}
```

## 单选按钮支付墙模式

如需将 PayPal 和分期付款作为独立单选项展示，须对单选行进行资格验证 — 永远不要为无法渲染的按钮显示单选选项：

```javascript
var payLaterButton = paypal.Buttons({
  fundingSource: paypal.FUNDING.PAYLATER,
  style: { color: 'blue', shape: 'rect', layout: 'vertical' },
  createOrder: createOrder,
  onApprove: onApprove,
  onError: onError
});

if (payLaterButton.isEligible()) {
  // 显示单选行及其内联消息
  document.getElementById('row-paylater').style.display = 'block';
  paypal.Marks({ fundingSource: paypal.FUNDING.PAYLATER }).render('#mark-paylater');
  payLaterButton.render('#button-paylater');
} else {
  // 隐藏整个单选行 — 该会话无法使用分期付款
  document.getElementById('row-paylater').style.display = 'none';
}
```

完整的单选按钮支付墙模式请参见 [[analysis-paypal-radio-button-payment-wall]]。

## React 集成（`@paypal/react-paypal-js`）

### Provider 配置

在 options 对象中传入 `locale` 和 `enableFunding`，根据页面语言提供不同的 `locale` 值：

```jsx
import { PayPalScriptProvider } from "@paypal/react-paypal-js";

// 英语站点
const PAYPAL_OPTIONS_EN = {
  clientId: "YOUR_CLIENT_ID",
  currency: "CAD",
  locale: "en_CA",
  components: "messages,buttons,funding-eligibility,marks",
  enableFunding: "paylater",
};

// 法语站点
const PAYPAL_OPTIONS_FR = {
  clientId: "YOUR_CLIENT_ID",
  currency: "CAD",
  locale: "fr_CA",
  components: "messages,buttons,funding-eligibility,marks",
  enableFunding: "paylater",
};

export default function App({ language }) {
  const options = language === "fr" ? PAYPAL_OPTIONS_FR : PAYPAL_OPTIONS_EN;
  return (
    <PayPalScriptProvider options={options}>
      <CheckoutPage language={language} />
    </PayPalScriptProvider>
  );
}
```

### SPA 语言切换

用户切换语言时，使用 `resetOptions` 重新加载 SDK：

```jsx
import { usePayPalScriptReducer } from "@paypal/react-paypal-js";

function LanguageSwitcher() {
  const [{ options }, dispatch] = usePayPalScriptReducer();

  function switchToFrench() {
    dispatch({
      type: "resetOptions",
      value: { ...options, locale: "fr_CA" },
    });
  }

  return <button onClick={switchToFrench}>Français</button>;
}
```

### 分期付款按钮 + 消息（完整加拿大示例）

```jsx
import {
  PayPalScriptProvider,
  PayPalButtons,
  PayPalMessages,
  PayPalMarks,
  FUNDING,
  usePayPalScriptReducer,
} from "@paypal/react-paypal-js";

// ── Provider — 放在应用根节点 ─────────────────────────────────────────────
const PAYPAL_OPTIONS = {
  clientId: "YOUR_CLIENT_ID",
  currency: "CAD",
  locale: "en_CA",             // 法语站点改为 "fr_CA"
  components: "messages,buttons,funding-eligibility,marks",
  enableFunding: "paylater",   // 加拿大商户必填
};

export default function App() {
  return (
    <PayPalScriptProvider options={PAYPAL_OPTIONS}>
      <CheckoutSection language="en-CA" amount={150.00} />
    </PayPalScriptProvider>
  );
}

// ── 结账区块 — 消息 + 图标 + 按钮 ────────────────────────────────────────
// language: "en-CA" | "fr-CA"
function CheckoutSection({ language, amount }) {
  const [{ isResolved }] = usePayPalScriptReducer();

  if (!isResolved) return <p>正在加载支付选项…</p>;

  return (
    <div>
      {/* 分期付款消息 — 显示在按钮上方 */}
      <PayPalMessages
        style={{
          layout: "text",
          logo: { type: "inline" },
          text: { color: "black", size: 12 },
        }}
        amount={amount}
        placement="payment"
        language={language}
      />

      {/* 分期付款图标 */}
      <div style={{ display: "flex", alignItems: "center", gap: 8, marginTop: 8 }}>
        <PayPalMarks fundingSource={FUNDING.PAYLATER} />
      </div>

      {/* 分期付款按钮 */}
      <PayPalButtons
        fundingSource={FUNDING.PAYLATER}
        style={{ color: "gold", shape: "rect", layout: "vertical" }}
        createOrder={(data, actions) =>
          actions.order.create({
            purchase_units: [{
              amount: { currency_code: "CAD", value: String(amount) },
            }],
          })
        }
        onApprove={(data, actions) =>
          actions.order.capture().then((details) => {
            console.log("订单已捕获：", details);
          })
        }
        onError={(err) => console.error(err)}
      >
        {/* 不符合资格时渲染 children — 返回 null 静默隐藏 */}
        {null}
      </PayPalButtons>
    </div>
  );
}
```

## 双语对照表

| 元素 | 英语 | 法语 |
| --- | --- | --- |
| SDK `locale` 参数 | `locale=en_CA` | `locale=fr_CA` |
| 消息 `data-pp-language` | `data-pp-language="en-CA"` | `data-pp-language="fr-CA"` |
| React `<PayPalMessages language>` | `language="en-CA"` | `language="fr-CA"` |
| React `PayPalScriptProvider locale` | `locale: "en_CA"` | `locale: "fr_CA"` |
| 按钮文字（SDK 渲染） | "Pay in 4" | "Payez en 4 fois" |

## 关键规则

| 规则 | 说明 |
| --- | --- |
| 需要加拿大商户账户 | 标准加拿大分期付款要求加拿大 PayPal 账户 — 与法国/美国跨境场景不同，无需额外审批 |
| `enable-funding=paylater` | **必填** — 缺少则分期付款按钮不会渲染 |
| `currency=CAD` | 必填 — 加拿大分期付款仅支持加拿大元 |
| 金额范围 | CAD $30–$1,500 — 超出范围消息自动隐藏；`isEligible()` 控制按钮显示 |
| 双语支持 | **必填** — 根据站点语言提供 `en_CA` 和 `fr_CA` |
| `locale` 与 `data-pp-language` 的区别 | `locale` 是 SDK URL 参数，控制按钮语言；`data-pp-language` 是每个消息元素的属性，控制消息语言 — 两者均需设置 |
| 禁止修改消息内容 | 不得翻译、调整大小、改变颜色或以任何方式修改分期付款消息文本 |
| 不支持循环付款 | 参考交易和循环付款集成不符合资格 |
| 每页只加载一次 SDK | 所有组件合并到单个 `<script>` 标签 |
| `Buttons()` 内的 `message` 选项 | **仅限美国商户 + 美国买家** — 本场景不适用；请使用带 `data-pp-language` 的独立 `data-pp-message` |

## 测试与上线

1. 沙箱测试使用 `client-id=test` 并添加 `buyer-country=CA`（仅限沙箱）模拟加拿大买家
2. 验证 Pay in 4 按钮渲染正常，消息在 `en_CA` 和 `fr_CA` 下均正确显示
3. 确认消息在低于 CAD $30 或高于 CAD $1,500 时自动隐藏
4. 上线时删除 `buyer-country=CA` 并替换为生产环境 `client-id`

```html
<!-- 仅用于沙箱测试 -->
<script
  src="https://www.paypal.com/sdk/js?client-id=test&buyer-country=CA&components=messages,buttons,funding-eligibility,marks&currency=CAD&enable-funding=paylater&locale=en_CA"
></script>
```

## 相关 Wiki 页面

- [[paypal-checkout]] — 基础 Checkout 集成
- [[paypal-pay-later]] — 各国分期付款产品详情
- [[analysis-paypal-radio-button-payment-wall]] — 带资格验证的单选按钮支付墙模式
- [[analysis-paypal-pay-later-fr-integration-guide]] — 跨境分期付款（非加拿大商户面向法国买家）

## 来源

- [[source-paypal-pay-later]] — 加拿大分期付款资格要求、双周还款周期、CAD $30–$1,500 范围、双语要求、`locale` 和 `data-pp-language` 参数
