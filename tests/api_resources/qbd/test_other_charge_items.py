# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor.types.qbd import (
    OtherChargeItem,
)
from conductor.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOtherChargeItems:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Conductor) -> None:
        other_charge_item = client.qbd.other_charge_items.create(
            name="Overnight Delivery",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(OtherChargeItem, other_charge_item, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Conductor) -> None:
        other_charge_item = client.qbd.other_charge_items.create(
            name="Overnight Delivery",
            conductor_end_user_id="end_usr_1234567abcdefg",
            barcode={
                "allow_override": False,
                "assign_even_if_used": False,
                "value": "012345678905",
            },
            class_id="80000001-1234567890",
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            is_active=True,
            parent_id="80000001-1234567890",
            sales_and_purchase_details={
                "expense_account_id": "80000001-1234567890",
                "income_account_id": "80000001-1234567890",
                "preferred_vendor_id": "80000001-1234567890",
                "purchase_cost": "15.75",
                "purchase_description": "Bulk purchase of steel bolts for inventory",
                "purchase_tax_code_id": "80000001-1234567890",
                "sales_description": "High-quality steel bolts suitable for construction",
                "sales_price": "19.99",
            },
            sales_or_purchase_details={
                "posting_account_id": "80000001-1234567890",
                "description": "Hourly Consulting Service",
                "price": "19.99",
                "price_percentage": "10.5",
            },
            sales_tax_code_id="80000001-1234567890",
        )
        assert_matches_type(OtherChargeItem, other_charge_item, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Conductor) -> None:
        response = client.qbd.other_charge_items.with_raw_response.create(
            name="Overnight Delivery",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        other_charge_item = response.parse()
        assert_matches_type(OtherChargeItem, other_charge_item, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Conductor) -> None:
        with client.qbd.other_charge_items.with_streaming_response.create(
            name="Overnight Delivery",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            other_charge_item = response.parse()
            assert_matches_type(OtherChargeItem, other_charge_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Conductor) -> None:
        other_charge_item = client.qbd.other_charge_items.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(OtherChargeItem, other_charge_item, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Conductor) -> None:
        response = client.qbd.other_charge_items.with_raw_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        other_charge_item = response.parse()
        assert_matches_type(OtherChargeItem, other_charge_item, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Conductor) -> None:
        with client.qbd.other_charge_items.with_streaming_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            other_charge_item = response.parse()
            assert_matches_type(OtherChargeItem, other_charge_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.other_charge_items.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_update(self, client: Conductor) -> None:
        other_charge_item = client.qbd.other_charge_items.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(OtherChargeItem, other_charge_item, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Conductor) -> None:
        other_charge_item = client.qbd.other_charge_items.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
            barcode={
                "allow_override": False,
                "assign_even_if_used": False,
                "value": "012345678905",
            },
            class_id="80000001-1234567890",
            is_active=True,
            name="Overnight Delivery",
            parent_id="80000001-1234567890",
            sales_and_purchase_details={
                "expense_account_id": "80000001-1234567890",
                "income_account_id": "80000001-1234567890",
                "preferred_vendor_id": "80000001-1234567890",
                "purchase_cost": "15.75",
                "purchase_description": "Bulk purchase of steel bolts for inventory",
                "purchase_tax_code_id": "80000001-1234567890",
                "sales_description": "High-quality steel bolts suitable for construction",
                "sales_price": "19.99",
                "update_existing_transactions_expense_account": False,
                "update_existing_transactions_income_account": False,
            },
            sales_or_purchase_details={
                "description": "Hourly Consulting Service",
                "posting_account_id": "80000001-1234567890",
                "price": "19.99",
                "price_percentage": "10.5",
                "update_existing_transactions_account": False,
            },
            sales_tax_code_id="80000001-1234567890",
        )
        assert_matches_type(OtherChargeItem, other_charge_item, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Conductor) -> None:
        response = client.qbd.other_charge_items.with_raw_response.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        other_charge_item = response.parse()
        assert_matches_type(OtherChargeItem, other_charge_item, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Conductor) -> None:
        with client.qbd.other_charge_items.with_streaming_response.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            other_charge_item = response.parse()
            assert_matches_type(OtherChargeItem, other_charge_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.other_charge_items.with_raw_response.update(
                id="",
                revision_number="1721172183",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_list(self, client: Conductor) -> None:
        other_charge_item = client.qbd.other_charge_items.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SyncCursorPage[OtherChargeItem], other_charge_item, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Conductor) -> None:
        other_charge_item = client.qbd.other_charge_items.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            class_ids=["80000001-1234567890"],
            cursor="12345678-abcd-abcd-example-1234567890ab",
            full_names=["Shipping Charges:Overnight Delivery"],
            ids=["80000001-1234567890"],
            limit=150,
            name_contains="ABC",
            name_ends_with="ABC",
            name_from="A",
            name_starts_with="ABC",
            name_to="Z",
            status="active",
            updated_after="2025-01-01T12:34:56+00:00",
            updated_before="2025-02-01T12:34:56+00:00",
        )
        assert_matches_type(SyncCursorPage[OtherChargeItem], other_charge_item, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Conductor) -> None:
        response = client.qbd.other_charge_items.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        other_charge_item = response.parse()
        assert_matches_type(SyncCursorPage[OtherChargeItem], other_charge_item, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Conductor) -> None:
        with client.qbd.other_charge_items.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            other_charge_item = response.parse()
            assert_matches_type(SyncCursorPage[OtherChargeItem], other_charge_item, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOtherChargeItems:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncConductor) -> None:
        other_charge_item = await async_client.qbd.other_charge_items.create(
            name="Overnight Delivery",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(OtherChargeItem, other_charge_item, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncConductor) -> None:
        other_charge_item = await async_client.qbd.other_charge_items.create(
            name="Overnight Delivery",
            conductor_end_user_id="end_usr_1234567abcdefg",
            barcode={
                "allow_override": False,
                "assign_even_if_used": False,
                "value": "012345678905",
            },
            class_id="80000001-1234567890",
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            is_active=True,
            parent_id="80000001-1234567890",
            sales_and_purchase_details={
                "expense_account_id": "80000001-1234567890",
                "income_account_id": "80000001-1234567890",
                "preferred_vendor_id": "80000001-1234567890",
                "purchase_cost": "15.75",
                "purchase_description": "Bulk purchase of steel bolts for inventory",
                "purchase_tax_code_id": "80000001-1234567890",
                "sales_description": "High-quality steel bolts suitable for construction",
                "sales_price": "19.99",
            },
            sales_or_purchase_details={
                "posting_account_id": "80000001-1234567890",
                "description": "Hourly Consulting Service",
                "price": "19.99",
                "price_percentage": "10.5",
            },
            sales_tax_code_id="80000001-1234567890",
        )
        assert_matches_type(OtherChargeItem, other_charge_item, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.other_charge_items.with_raw_response.create(
            name="Overnight Delivery",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        other_charge_item = await response.parse()
        assert_matches_type(OtherChargeItem, other_charge_item, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.other_charge_items.with_streaming_response.create(
            name="Overnight Delivery",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            other_charge_item = await response.parse()
            assert_matches_type(OtherChargeItem, other_charge_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncConductor) -> None:
        other_charge_item = await async_client.qbd.other_charge_items.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(OtherChargeItem, other_charge_item, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.other_charge_items.with_raw_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        other_charge_item = await response.parse()
        assert_matches_type(OtherChargeItem, other_charge_item, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.other_charge_items.with_streaming_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            other_charge_item = await response.parse()
            assert_matches_type(OtherChargeItem, other_charge_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.other_charge_items.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncConductor) -> None:
        other_charge_item = await async_client.qbd.other_charge_items.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(OtherChargeItem, other_charge_item, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncConductor) -> None:
        other_charge_item = await async_client.qbd.other_charge_items.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
            barcode={
                "allow_override": False,
                "assign_even_if_used": False,
                "value": "012345678905",
            },
            class_id="80000001-1234567890",
            is_active=True,
            name="Overnight Delivery",
            parent_id="80000001-1234567890",
            sales_and_purchase_details={
                "expense_account_id": "80000001-1234567890",
                "income_account_id": "80000001-1234567890",
                "preferred_vendor_id": "80000001-1234567890",
                "purchase_cost": "15.75",
                "purchase_description": "Bulk purchase of steel bolts for inventory",
                "purchase_tax_code_id": "80000001-1234567890",
                "sales_description": "High-quality steel bolts suitable for construction",
                "sales_price": "19.99",
                "update_existing_transactions_expense_account": False,
                "update_existing_transactions_income_account": False,
            },
            sales_or_purchase_details={
                "description": "Hourly Consulting Service",
                "posting_account_id": "80000001-1234567890",
                "price": "19.99",
                "price_percentage": "10.5",
                "update_existing_transactions_account": False,
            },
            sales_tax_code_id="80000001-1234567890",
        )
        assert_matches_type(OtherChargeItem, other_charge_item, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.other_charge_items.with_raw_response.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        other_charge_item = await response.parse()
        assert_matches_type(OtherChargeItem, other_charge_item, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.other_charge_items.with_streaming_response.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            other_charge_item = await response.parse()
            assert_matches_type(OtherChargeItem, other_charge_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.other_charge_items.with_raw_response.update(
                id="",
                revision_number="1721172183",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncConductor) -> None:
        other_charge_item = await async_client.qbd.other_charge_items.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(AsyncCursorPage[OtherChargeItem], other_charge_item, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncConductor) -> None:
        other_charge_item = await async_client.qbd.other_charge_items.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            class_ids=["80000001-1234567890"],
            cursor="12345678-abcd-abcd-example-1234567890ab",
            full_names=["Shipping Charges:Overnight Delivery"],
            ids=["80000001-1234567890"],
            limit=150,
            name_contains="ABC",
            name_ends_with="ABC",
            name_from="A",
            name_starts_with="ABC",
            name_to="Z",
            status="active",
            updated_after="2025-01-01T12:34:56+00:00",
            updated_before="2025-02-01T12:34:56+00:00",
        )
        assert_matches_type(AsyncCursorPage[OtherChargeItem], other_charge_item, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.other_charge_items.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        other_charge_item = await response.parse()
        assert_matches_type(AsyncCursorPage[OtherChargeItem], other_charge_item, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.other_charge_items.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            other_charge_item = await response.parse()
            assert_matches_type(AsyncCursorPage[OtherChargeItem], other_charge_item, path=["response"])

        assert cast(Any, response.is_closed) is True
