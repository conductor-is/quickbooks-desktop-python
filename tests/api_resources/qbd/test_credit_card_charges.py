# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor._utils import parse_date
from conductor.types.qbd import (
    CreditCardCharge,
    CreditCardChargeDeleteResponse,
)
from conductor.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCreditCardCharges:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Conductor) -> None:
        credit_card_charge = client.qbd.credit_card_charges.create(
            account_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(CreditCardCharge, credit_card_charge, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Conductor) -> None:
        credit_card_charge = client.qbd.credit_card_charges.create(
            account_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
            exchange_rate=1.2345,
            expense_lines=[
                {
                    "account_id": "80000001-1234567890",
                    "amount": "1000.00",
                    "billing_status": "billable",
                    "class_id": "80000001-1234567890",
                    "custom_fields": [
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        }
                    ],
                    "memo": "New office chair",
                    "payee_id": "80000001-1234567890",
                    "sales_representative_id": "80000001-1234567890",
                    "sales_tax_code_id": "80000001-1234567890",
                }
            ],
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            item_group_lines=[
                {
                    "item_group_id": "80000001-1234567890",
                    "custom_fields": [
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        }
                    ],
                    "inventory_site_id": "80000001-1234567890",
                    "inventory_site_location_id": "80000001-1234567890",
                    "quantity": 5,
                    "unit_of_measure": "Each",
                }
            ],
            item_lines=[
                {
                    "amount": "1000.00",
                    "billing_status": "billable",
                    "class_id": "80000001-1234567890",
                    "cost": "1000.00",
                    "customer_id": "80000001-1234567890",
                    "custom_fields": [
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        }
                    ],
                    "description": "High-quality widget with custom engraving",
                    "expiration_date": parse_date("2025-12-31"),
                    "inventory_site_id": "80000001-1234567890",
                    "inventory_site_location_id": "80000001-1234567890",
                    "item_id": "80000001-1234567890",
                    "link_to_transaction_line": {
                        "transaction_id": "123ABC-1234567890",
                        "transaction_line_id": "456DEF-1234567890",
                    },
                    "lot_number": "LOT2023-001",
                    "override_item_account_id": "80000001-1234567890",
                    "quantity": 5,
                    "sales_representative_id": "80000001-1234567890",
                    "sales_tax_code_id": "80000001-1234567890",
                    "serial_number": "SN1234567890",
                    "unit_of_measure": "Each",
                }
            ],
            memo="Office supplies for Q3 marketing campaign",
            payee_id="80000001-1234567890",
            ref_number="CARD-1234",
            sales_tax_code_id="80000001-1234567890",
        )
        assert_matches_type(CreditCardCharge, credit_card_charge, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Conductor) -> None:
        response = client.qbd.credit_card_charges.with_raw_response.create(
            account_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_card_charge = response.parse()
        assert_matches_type(CreditCardCharge, credit_card_charge, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Conductor) -> None:
        with client.qbd.credit_card_charges.with_streaming_response.create(
            account_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_card_charge = response.parse()
            assert_matches_type(CreditCardCharge, credit_card_charge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Conductor) -> None:
        credit_card_charge = client.qbd.credit_card_charges.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(CreditCardCharge, credit_card_charge, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Conductor) -> None:
        response = client.qbd.credit_card_charges.with_raw_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_card_charge = response.parse()
        assert_matches_type(CreditCardCharge, credit_card_charge, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Conductor) -> None:
        with client.qbd.credit_card_charges.with_streaming_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_card_charge = response.parse()
            assert_matches_type(CreditCardCharge, credit_card_charge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.credit_card_charges.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_update(self, client: Conductor) -> None:
        credit_card_charge = client.qbd.credit_card_charges.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(CreditCardCharge, credit_card_charge, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Conductor) -> None:
        credit_card_charge = client.qbd.credit_card_charges.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_id="80000001-1234567890",
            clear_expense_lines=False,
            clear_item_lines=False,
            exchange_rate=1.2345,
            expense_lines=[
                {
                    "id": "456DEF-1234567890",
                    "account_id": "80000001-1234567890",
                    "amount": "1000.00",
                    "billing_status": "billable",
                    "class_id": "80000001-1234567890",
                    "memo": "New office chair",
                    "payee_id": "80000001-1234567890",
                    "sales_representative_id": "80000001-1234567890",
                    "sales_tax_code_id": "80000001-1234567890",
                }
            ],
            item_group_lines=[
                {
                    "id": "456DEF-1234567890",
                    "item_group_id": "80000001-1234567890",
                    "item_lines": [
                        {
                            "id": "456DEF-1234567890",
                            "amount": "1000.00",
                            "billing_status": "billable",
                            "class_id": "80000001-1234567890",
                            "cost": "1000.00",
                            "customer_id": "80000001-1234567890",
                            "description": "High-quality widget with custom engraving",
                            "expiration_date": parse_date("2025-12-31"),
                            "inventory_site_id": "80000001-1234567890",
                            "inventory_site_location_id": "80000001-1234567890",
                            "item_id": "80000001-1234567890",
                            "lot_number": "LOT2023-001",
                            "override_item_account_id": "80000001-1234567890",
                            "override_unit_of_measure_set_id": "80000001-1234567890",
                            "quantity": 5,
                            "sales_representative_id": "80000001-1234567890",
                            "sales_tax_code_id": "80000001-1234567890",
                            "serial_number": "SN1234567890",
                            "unit_of_measure": "Each",
                        }
                    ],
                    "override_unit_of_measure_set_id": "80000001-1234567890",
                    "quantity": 5,
                    "unit_of_measure": "Each",
                }
            ],
            item_lines=[
                {
                    "id": "456DEF-1234567890",
                    "amount": "1000.00",
                    "billing_status": "billable",
                    "class_id": "80000001-1234567890",
                    "cost": "1000.00",
                    "customer_id": "80000001-1234567890",
                    "description": "High-quality widget with custom engraving",
                    "expiration_date": parse_date("2025-12-31"),
                    "inventory_site_id": "80000001-1234567890",
                    "inventory_site_location_id": "80000001-1234567890",
                    "item_id": "80000001-1234567890",
                    "lot_number": "LOT2023-001",
                    "override_item_account_id": "80000001-1234567890",
                    "override_unit_of_measure_set_id": "80000001-1234567890",
                    "quantity": 5,
                    "sales_representative_id": "80000001-1234567890",
                    "sales_tax_code_id": "80000001-1234567890",
                    "serial_number": "SN1234567890",
                    "unit_of_measure": "Each",
                }
            ],
            memo="Office supplies for Q3 marketing campaign",
            payee_id="80000001-1234567890",
            ref_number="CARD-1234",
            sales_tax_code_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
        )
        assert_matches_type(CreditCardCharge, credit_card_charge, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Conductor) -> None:
        response = client.qbd.credit_card_charges.with_raw_response.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_card_charge = response.parse()
        assert_matches_type(CreditCardCharge, credit_card_charge, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Conductor) -> None:
        with client.qbd.credit_card_charges.with_streaming_response.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_card_charge = response.parse()
            assert_matches_type(CreditCardCharge, credit_card_charge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.credit_card_charges.with_raw_response.update(
                id="",
                revision_number="1721172183",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_list(self, client: Conductor) -> None:
        credit_card_charge = client.qbd.credit_card_charges.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SyncCursorPage[CreditCardCharge], credit_card_charge, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Conductor) -> None:
        credit_card_charge = client.qbd.credit_card_charges.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_ids=["80000001-1234567890"],
            currency_ids=["80000001-1234567890"],
            cursor="12345678-abcd-abcd-example-1234567890ab",
            ids=["123ABC-1234567890"],
            include_line_items=True,
            limit=150,
            payee_ids=["80000001-1234567890"],
            ref_number_contains="CARD-1234",
            ref_number_ends_with="1234",
            ref_number_from="CARD-0001",
            ref_numbers=["CREDIT CARD CHARGE-1234"],
            ref_number_starts_with="CARD",
            ref_number_to="CARD-9999",
            transaction_date_from=parse_date("2025-01-01"),
            transaction_date_to=parse_date("2025-02-01"),
            updated_after="2025-01-01T12:34:56+00:00",
            updated_before="2025-02-01T12:34:56+00:00",
        )
        assert_matches_type(SyncCursorPage[CreditCardCharge], credit_card_charge, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Conductor) -> None:
        response = client.qbd.credit_card_charges.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_card_charge = response.parse()
        assert_matches_type(SyncCursorPage[CreditCardCharge], credit_card_charge, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Conductor) -> None:
        with client.qbd.credit_card_charges.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_card_charge = response.parse()
            assert_matches_type(SyncCursorPage[CreditCardCharge], credit_card_charge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Conductor) -> None:
        credit_card_charge = client.qbd.credit_card_charges.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(CreditCardChargeDeleteResponse, credit_card_charge, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Conductor) -> None:
        response = client.qbd.credit_card_charges.with_raw_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_card_charge = response.parse()
        assert_matches_type(CreditCardChargeDeleteResponse, credit_card_charge, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Conductor) -> None:
        with client.qbd.credit_card_charges.with_streaming_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_card_charge = response.parse()
            assert_matches_type(CreditCardChargeDeleteResponse, credit_card_charge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.credit_card_charges.with_raw_response.delete(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )


class TestAsyncCreditCardCharges:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncConductor) -> None:
        credit_card_charge = await async_client.qbd.credit_card_charges.create(
            account_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(CreditCardCharge, credit_card_charge, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncConductor) -> None:
        credit_card_charge = await async_client.qbd.credit_card_charges.create(
            account_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
            exchange_rate=1.2345,
            expense_lines=[
                {
                    "account_id": "80000001-1234567890",
                    "amount": "1000.00",
                    "billing_status": "billable",
                    "class_id": "80000001-1234567890",
                    "custom_fields": [
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        }
                    ],
                    "memo": "New office chair",
                    "payee_id": "80000001-1234567890",
                    "sales_representative_id": "80000001-1234567890",
                    "sales_tax_code_id": "80000001-1234567890",
                }
            ],
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            item_group_lines=[
                {
                    "item_group_id": "80000001-1234567890",
                    "custom_fields": [
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        }
                    ],
                    "inventory_site_id": "80000001-1234567890",
                    "inventory_site_location_id": "80000001-1234567890",
                    "quantity": 5,
                    "unit_of_measure": "Each",
                }
            ],
            item_lines=[
                {
                    "amount": "1000.00",
                    "billing_status": "billable",
                    "class_id": "80000001-1234567890",
                    "cost": "1000.00",
                    "customer_id": "80000001-1234567890",
                    "custom_fields": [
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        }
                    ],
                    "description": "High-quality widget with custom engraving",
                    "expiration_date": parse_date("2025-12-31"),
                    "inventory_site_id": "80000001-1234567890",
                    "inventory_site_location_id": "80000001-1234567890",
                    "item_id": "80000001-1234567890",
                    "link_to_transaction_line": {
                        "transaction_id": "123ABC-1234567890",
                        "transaction_line_id": "456DEF-1234567890",
                    },
                    "lot_number": "LOT2023-001",
                    "override_item_account_id": "80000001-1234567890",
                    "quantity": 5,
                    "sales_representative_id": "80000001-1234567890",
                    "sales_tax_code_id": "80000001-1234567890",
                    "serial_number": "SN1234567890",
                    "unit_of_measure": "Each",
                }
            ],
            memo="Office supplies for Q3 marketing campaign",
            payee_id="80000001-1234567890",
            ref_number="CARD-1234",
            sales_tax_code_id="80000001-1234567890",
        )
        assert_matches_type(CreditCardCharge, credit_card_charge, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.credit_card_charges.with_raw_response.create(
            account_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_card_charge = await response.parse()
        assert_matches_type(CreditCardCharge, credit_card_charge, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.credit_card_charges.with_streaming_response.create(
            account_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_card_charge = await response.parse()
            assert_matches_type(CreditCardCharge, credit_card_charge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncConductor) -> None:
        credit_card_charge = await async_client.qbd.credit_card_charges.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(CreditCardCharge, credit_card_charge, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.credit_card_charges.with_raw_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_card_charge = await response.parse()
        assert_matches_type(CreditCardCharge, credit_card_charge, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.credit_card_charges.with_streaming_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_card_charge = await response.parse()
            assert_matches_type(CreditCardCharge, credit_card_charge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.credit_card_charges.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncConductor) -> None:
        credit_card_charge = await async_client.qbd.credit_card_charges.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(CreditCardCharge, credit_card_charge, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncConductor) -> None:
        credit_card_charge = await async_client.qbd.credit_card_charges.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_id="80000001-1234567890",
            clear_expense_lines=False,
            clear_item_lines=False,
            exchange_rate=1.2345,
            expense_lines=[
                {
                    "id": "456DEF-1234567890",
                    "account_id": "80000001-1234567890",
                    "amount": "1000.00",
                    "billing_status": "billable",
                    "class_id": "80000001-1234567890",
                    "memo": "New office chair",
                    "payee_id": "80000001-1234567890",
                    "sales_representative_id": "80000001-1234567890",
                    "sales_tax_code_id": "80000001-1234567890",
                }
            ],
            item_group_lines=[
                {
                    "id": "456DEF-1234567890",
                    "item_group_id": "80000001-1234567890",
                    "item_lines": [
                        {
                            "id": "456DEF-1234567890",
                            "amount": "1000.00",
                            "billing_status": "billable",
                            "class_id": "80000001-1234567890",
                            "cost": "1000.00",
                            "customer_id": "80000001-1234567890",
                            "description": "High-quality widget with custom engraving",
                            "expiration_date": parse_date("2025-12-31"),
                            "inventory_site_id": "80000001-1234567890",
                            "inventory_site_location_id": "80000001-1234567890",
                            "item_id": "80000001-1234567890",
                            "lot_number": "LOT2023-001",
                            "override_item_account_id": "80000001-1234567890",
                            "override_unit_of_measure_set_id": "80000001-1234567890",
                            "quantity": 5,
                            "sales_representative_id": "80000001-1234567890",
                            "sales_tax_code_id": "80000001-1234567890",
                            "serial_number": "SN1234567890",
                            "unit_of_measure": "Each",
                        }
                    ],
                    "override_unit_of_measure_set_id": "80000001-1234567890",
                    "quantity": 5,
                    "unit_of_measure": "Each",
                }
            ],
            item_lines=[
                {
                    "id": "456DEF-1234567890",
                    "amount": "1000.00",
                    "billing_status": "billable",
                    "class_id": "80000001-1234567890",
                    "cost": "1000.00",
                    "customer_id": "80000001-1234567890",
                    "description": "High-quality widget with custom engraving",
                    "expiration_date": parse_date("2025-12-31"),
                    "inventory_site_id": "80000001-1234567890",
                    "inventory_site_location_id": "80000001-1234567890",
                    "item_id": "80000001-1234567890",
                    "lot_number": "LOT2023-001",
                    "override_item_account_id": "80000001-1234567890",
                    "override_unit_of_measure_set_id": "80000001-1234567890",
                    "quantity": 5,
                    "sales_representative_id": "80000001-1234567890",
                    "sales_tax_code_id": "80000001-1234567890",
                    "serial_number": "SN1234567890",
                    "unit_of_measure": "Each",
                }
            ],
            memo="Office supplies for Q3 marketing campaign",
            payee_id="80000001-1234567890",
            ref_number="CARD-1234",
            sales_tax_code_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
        )
        assert_matches_type(CreditCardCharge, credit_card_charge, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.credit_card_charges.with_raw_response.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_card_charge = await response.parse()
        assert_matches_type(CreditCardCharge, credit_card_charge, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.credit_card_charges.with_streaming_response.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_card_charge = await response.parse()
            assert_matches_type(CreditCardCharge, credit_card_charge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.credit_card_charges.with_raw_response.update(
                id="",
                revision_number="1721172183",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncConductor) -> None:
        credit_card_charge = await async_client.qbd.credit_card_charges.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(AsyncCursorPage[CreditCardCharge], credit_card_charge, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncConductor) -> None:
        credit_card_charge = await async_client.qbd.credit_card_charges.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_ids=["80000001-1234567890"],
            currency_ids=["80000001-1234567890"],
            cursor="12345678-abcd-abcd-example-1234567890ab",
            ids=["123ABC-1234567890"],
            include_line_items=True,
            limit=150,
            payee_ids=["80000001-1234567890"],
            ref_number_contains="CARD-1234",
            ref_number_ends_with="1234",
            ref_number_from="CARD-0001",
            ref_numbers=["CREDIT CARD CHARGE-1234"],
            ref_number_starts_with="CARD",
            ref_number_to="CARD-9999",
            transaction_date_from=parse_date("2025-01-01"),
            transaction_date_to=parse_date("2025-02-01"),
            updated_after="2025-01-01T12:34:56+00:00",
            updated_before="2025-02-01T12:34:56+00:00",
        )
        assert_matches_type(AsyncCursorPage[CreditCardCharge], credit_card_charge, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.credit_card_charges.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_card_charge = await response.parse()
        assert_matches_type(AsyncCursorPage[CreditCardCharge], credit_card_charge, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.credit_card_charges.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_card_charge = await response.parse()
            assert_matches_type(AsyncCursorPage[CreditCardCharge], credit_card_charge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncConductor) -> None:
        credit_card_charge = await async_client.qbd.credit_card_charges.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(CreditCardChargeDeleteResponse, credit_card_charge, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.credit_card_charges.with_raw_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_card_charge = await response.parse()
        assert_matches_type(CreditCardChargeDeleteResponse, credit_card_charge, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.credit_card_charges.with_streaming_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_card_charge = await response.parse()
            assert_matches_type(CreditCardChargeDeleteResponse, credit_card_charge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.credit_card_charges.with_raw_response.delete(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )
