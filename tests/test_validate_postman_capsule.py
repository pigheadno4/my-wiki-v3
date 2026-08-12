import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_postman_capsule import (  # noqa: E402
    PostmanCapsuleValidationError,
    validate_postman_capsule,
)


SCHEMA_V21 = "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"


def write_text(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def write_json(path, payload):
    write_text(path, json.dumps(payload))


class PostmanCapsuleValidationTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.snapshot = Path(self.directory.name)
        self.postman_path = "postman/CheckoutService-v72.json"
        self.sentinel_path = ".github/workflows/sync-collections.yml"

    def test_accepts_v21_collections_and_complete_sentinel(self):
        write_json(
            self.snapshot / "files" / self.postman_path,
            {"info": {"schema": SCHEMA_V21}, "item": []},
        )
        write_text(
            self.snapshot / "files" / self.sentinel_path,
            "CheckoutService-v72.json\nRecurringService-v68.json\n",
        )

        result = validate_postman_capsule(
            self.snapshot,
            (self.postman_path,),
            self.sentinel_path,
            ("CheckoutService-v72.json", "RecurringService-v68.json"),
        )

        self.assertEqual(1, result.postman_file_count)
        self.assertEqual(2, result.sentinel_reference_count)

    def test_rejects_invalid_json(self):
        write_text(self.snapshot / "files" / self.postman_path, "{")

        with self.assertRaisesRegex(
            PostmanCapsuleValidationError,
            r"invalid-postman-json: postman/CheckoutService-v72\.json",
        ):
            validate_postman_capsule(
                self.snapshot,
                (self.postman_path,),
                self.sentinel_path,
                ("CheckoutService-v72.json",),
            )

    def test_rejects_wrong_postman_schema(self):
        write_json(
            self.snapshot / "files" / self.postman_path,
            {
                "info": {
                    "schema": "https://schema.getpostman.com/json/collection/v2.0.0/collection.json"
                }
            },
        )

        with self.assertRaisesRegex(
            PostmanCapsuleValidationError,
            r"wrong-postman-schema: postman/CheckoutService-v72\.json",
        ):
            validate_postman_capsule(
                self.snapshot,
                (self.postman_path,),
                self.sentinel_path,
                ("CheckoutService-v72.json",),
            )

    def test_rejects_missing_sentinel_reference(self):
        write_json(
            self.snapshot / "files" / self.postman_path,
            {"info": {"schema": SCHEMA_V21}},
        )
        write_text(
            self.snapshot / "files" / self.sentinel_path,
            "CheckoutService-v72.json\n",
        )

        with self.assertRaisesRegex(
            PostmanCapsuleValidationError,
            "missing-sentinel-reference: RecurringService-v68.json",
        ):
            validate_postman_capsule(
                self.snapshot,
                (self.postman_path,),
                self.sentinel_path,
                ("CheckoutService-v72.json", "RecurringService-v68.json"),
            )

    def test_rejects_missing_selected_file(self):
        with self.assertRaisesRegex(
            PostmanCapsuleValidationError,
            r"missing-postman-file: postman/CheckoutService-v72\.json",
        ):
            validate_postman_capsule(
                self.snapshot,
                (self.postman_path,),
                self.sentinel_path,
                ("CheckoutService-v72.json",),
            )


if __name__ == "__main__":
    unittest.main()
