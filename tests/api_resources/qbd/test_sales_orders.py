# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor._utils import parse_date
from conductor.types.qbd import (
    SalesOrder,
    SalesOrderDeleteResponse,
)
from conductor.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSalesOrders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Conductor) -> None:
        sales_order = client.qbd.sales_orders.create(
            customer_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SalesOrder, sales_order, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Conductor) -> None:
        sales_order = client.qbd.sales_orders.create(
            customer_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
            billing_address={
                "city": "San Francisco",
                "country": "United States",
                "line1": "Conductor Labs Inc.",
                "line2": "540 Market St.",
                "line3": "Suite 100",
                "line4": "",
                "line5": "",
                "note": "Conductor HQ",
                "postal_code": "94110",
                "state": "CA",
            },
            class_id="80000001-1234567890",
            customer_message_id="80000001-1234567890",
            document_template_id="80000001-1234567890",
            due_date=parse_date("2024-10-31"),
            exchange_rate=1.2345,
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            is_manually_closed=True,
            is_queued_for_email=True,
            is_queued_for_print=True,
            line_groups=[
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
            lines=[
                {
                    "amount": "1000.00",
                    "class_id": "80000001-1234567890",
                    "custom_fields": [
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        }
                    ],
                    "description": "Widget Model X100 - Blue",
                    "inventory_site_id": "80000001-1234567890",
                    "inventory_site_location_id": "80000001-1234567890",
                    "is_manually_closed": True,
                    "item_id": "80000001-1234567890",
                    "lot_number": "LOT2023-001",
                    "other_custom_field1": "Special handling required",
                    "other_custom_field2": "Always ship with a spare",
                    "price_level_id": "80000001-1234567890",
                    "price_rule_conflict_strategy": "base_price",
                    "quantity": 5,
                    "rate": "10.00",
                    "rate_percent": "10.5",
                    "sales_tax_code_id": "80000001-1234567890",
                    "serial_number": "SN1234567890",
                    "unit_of_measure": "Each",
                }
            ],
            memo="Customer requested rush delivery",
            other_custom_field="Special handling required",
            purchase_order_number="PO-1234",
            ref_number="SO-1234",
            sales_channel_name="ecommerce",
            sales_representative_id="80000001-1234567890",
            sales_store_name="Store 1",
            sales_store_type="Retail",
            sales_tax_code_id="80000001-1234567890",
            sales_tax_item_id="80000001-1234567890",
            shipment_origin="San Francisco, CA",
            shipping_address={
                "city": "San Francisco",
                "country": "United States",
                "line1": "Conductor Labs Inc.",
                "line2": "540 Market St.",
                "line3": "Suite 100",
                "line4": "",
                "line5": "",
                "note": "Conductor HQ",
                "postal_code": "94110",
                "state": "CA",
            },
            shipping_date=parse_date("2024-10-01"),
            shipping_method_id="80000001-1234567890",
            terms_id="80000001-1234567890",
        )
        assert_matches_type(SalesOrder, sales_order, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Conductor) -> None:
        response = client.qbd.sales_orders.with_raw_response.create(
            customer_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sales_order = response.parse()
        assert_matches_type(SalesOrder, sales_order, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Conductor) -> None:
        with client.qbd.sales_orders.with_streaming_response.create(
            customer_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sales_order = response.parse()
            assert_matches_type(SalesOrder, sales_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Conductor) -> None:
        sales_order = client.qbd.sales_orders.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SalesOrder, sales_order, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Conductor) -> None:
        response = client.qbd.sales_orders.with_raw_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sales_order = response.parse()
        assert_matches_type(SalesOrder, sales_order, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Conductor) -> None:
        with client.qbd.sales_orders.with_streaming_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sales_order = response.parse()
            assert_matches_type(SalesOrder, sales_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.sales_orders.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_update(self, client: Conductor) -> None:
        sales_order = client.qbd.sales_orders.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SalesOrder, sales_order, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Conductor) -> None:
        sales_order = client.qbd.sales_orders.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
            billing_address={
                "city": "San Francisco",
                "country": "United States",
                "line1": "Conductor Labs Inc.",
                "line2": "540 Market St.",
                "line3": "Suite 100",
                "line4": "",
                "line5": "",
                "note": "Conductor HQ",
                "postal_code": "94110",
                "state": "CA",
            },
            class_id="80000001-1234567890",
            customer_id="80000001-1234567890",
            customer_message_id="80000001-1234567890",
            document_template_id="80000001-1234567890",
            due_date=parse_date("2024-10-31"),
            exchange_rate=1.2345,
            is_manually_closed=True,
            is_queued_for_email=True,
            is_queued_for_print=True,
            line_groups=[
                {
                    "id": "456DEF-1234567890",
                    "item_group_id": "80000001-1234567890",
                    "lines": [
                        {
                            "id": "456DEF-1234567890",
                            "amount": "1000.00",
                            "class_id": "80000001-1234567890",
                            "description": "Widget Model X100 - Blue",
                            "inventory_site_id": "80000001-1234567890",
                            "inventory_site_location_id": "80000001-1234567890",
                            "is_manually_closed": True,
                            "item_id": "80000001-1234567890",
                            "lot_number": "LOT2023-001",
                            "other_custom_field1": "Special handling required",
                            "other_custom_field2": "Always ship with a spare",
                            "override_unit_of_measure_set_id": "80000001-1234567890",
                            "price_level_id": "80000001-1234567890",
                            "price_rule_conflict_strategy": "base_price",
                            "quantity": 5,
                            "rate": "10.00",
                            "rate_percent": "10.5",
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
            lines=[
                {
                    "id": "456DEF-1234567890",
                    "amount": "1000.00",
                    "class_id": "80000001-1234567890",
                    "description": "Widget Model X100 - Blue",
                    "inventory_site_id": "80000001-1234567890",
                    "inventory_site_location_id": "80000001-1234567890",
                    "is_manually_closed": True,
                    "item_id": "80000001-1234567890",
                    "lot_number": "LOT2023-001",
                    "other_custom_field1": "Special handling required",
                    "other_custom_field2": "Always ship with a spare",
                    "override_unit_of_measure_set_id": "80000001-1234567890",
                    "price_level_id": "80000001-1234567890",
                    "price_rule_conflict_strategy": "base_price",
                    "quantity": 5,
                    "rate": "10.00",
                    "rate_percent": "10.5",
                    "sales_tax_code_id": "80000001-1234567890",
                    "serial_number": "SN1234567890",
                    "unit_of_measure": "Each",
                }
            ],
            memo="Customer requested rush delivery",
            other_custom_field="Special handling required",
            purchase_order_number="PO-1234",
            ref_number="SO-1234",
            sales_channel_name="ecommerce",
            sales_representative_id="80000001-1234567890",
            sales_store_name="Store 1",
            sales_store_type="Retail",
            sales_tax_code_id="80000001-1234567890",
            sales_tax_item_id="80000001-1234567890",
            shipment_origin="San Francisco, CA",
            shipping_address={
                "city": "San Francisco",
                "country": "United States",
                "line1": "Conductor Labs Inc.",
                "line2": "540 Market St.",
                "line3": "Suite 100",
                "line4": "",
                "line5": "",
                "note": "Conductor HQ",
                "postal_code": "94110",
                "state": "CA",
            },
            shipping_date=parse_date("2024-10-01"),
            shipping_method_id="80000001-1234567890",
            terms_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
        )
        assert_matches_type(SalesOrder, sales_order, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Conductor) -> None:
        response = client.qbd.sales_orders.with_raw_response.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sales_order = response.parse()
        assert_matches_type(SalesOrder, sales_order, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Conductor) -> None:
        with client.qbd.sales_orders.with_streaming_response.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sales_order = response.parse()
            assert_matches_type(SalesOrder, sales_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.sales_orders.with_raw_response.update(
                id="",
                revision_number="1721172183",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_list(self, client: Conductor) -> None:
        sales_order = client.qbd.sales_orders.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SyncCursorPage[SalesOrder], sales_order, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Conductor) -> None:
        sales_order = client.qbd.sales_orders.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            currency_ids=["80000001-1234567890"],
            cursor="12345678-abcd-abcd-example-1234567890ab",
            customer_ids=["80000001-1234567890"],
            ids=["123ABC-1234567890"],
            include_line_items=True,
            include_linked_transactions=False,
            limit=150,
            ref_number_contains="SO-1234",
            ref_number_ends_with="1234",
            ref_number_from="SO-0001",
            ref_numbers=["SALES ORDER-1234"],
            ref_number_starts_with="SO",
            ref_number_to="SO-9999",
            transaction_date_from=parse_date("2025-01-01"),
            transaction_date_to=parse_date("2025-02-01"),
            updated_after="2025-01-01T12:34:56+00:00",
            updated_before="2025-02-01T12:34:56+00:00",
        )
        assert_matches_type(SyncCursorPage[SalesOrder], sales_order, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Conductor) -> None:
        response = client.qbd.sales_orders.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sales_order = response.parse()
        assert_matches_type(SyncCursorPage[SalesOrder], sales_order, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Conductor) -> None:
        with client.qbd.sales_orders.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sales_order = response.parse()
            assert_matches_type(SyncCursorPage[SalesOrder], sales_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Conductor) -> None:
        sales_order = client.qbd.sales_orders.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SalesOrderDeleteResponse, sales_order, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Conductor) -> None:
        response = client.qbd.sales_orders.with_raw_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sales_order = response.parse()
        assert_matches_type(SalesOrderDeleteResponse, sales_order, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Conductor) -> None:
        with client.qbd.sales_orders.with_streaming_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sales_order = response.parse()
            assert_matches_type(SalesOrderDeleteResponse, sales_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.sales_orders.with_raw_response.delete(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )


class TestAsyncSalesOrders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncConductor) -> None:
        sales_order = await async_client.qbd.sales_orders.create(
            customer_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SalesOrder, sales_order, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncConductor) -> None:
        sales_order = await async_client.qbd.sales_orders.create(
            customer_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
            billing_address={
                "city": "San Francisco",
                "country": "United States",
                "line1": "Conductor Labs Inc.",
                "line2": "540 Market St.",
                "line3": "Suite 100",
                "line4": "",
                "line5": "",
                "note": "Conductor HQ",
                "postal_code": "94110",
                "state": "CA",
            },
            class_id="80000001-1234567890",
            customer_message_id="80000001-1234567890",
            document_template_id="80000001-1234567890",
            due_date=parse_date("2024-10-31"),
            exchange_rate=1.2345,
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            is_manually_closed=True,
            is_queued_for_email=True,
            is_queued_for_print=True,
            line_groups=[
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
            lines=[
                {
                    "amount": "1000.00",
                    "class_id": "80000001-1234567890",
                    "custom_fields": [
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        }
                    ],
                    "description": "Widget Model X100 - Blue",
                    "inventory_site_id": "80000001-1234567890",
                    "inventory_site_location_id": "80000001-1234567890",
                    "is_manually_closed": True,
                    "item_id": "80000001-1234567890",
                    "lot_number": "LOT2023-001",
                    "other_custom_field1": "Special handling required",
                    "other_custom_field2": "Always ship with a spare",
                    "price_level_id": "80000001-1234567890",
                    "price_rule_conflict_strategy": "base_price",
                    "quantity": 5,
                    "rate": "10.00",
                    "rate_percent": "10.5",
                    "sales_tax_code_id": "80000001-1234567890",
                    "serial_number": "SN1234567890",
                    "unit_of_measure": "Each",
                }
            ],
            memo="Customer requested rush delivery",
            other_custom_field="Special handling required",
            purchase_order_number="PO-1234",
            ref_number="SO-1234",
            sales_channel_name="ecommerce",
            sales_representative_id="80000001-1234567890",
            sales_store_name="Store 1",
            sales_store_type="Retail",
            sales_tax_code_id="80000001-1234567890",
            sales_tax_item_id="80000001-1234567890",
            shipment_origin="San Francisco, CA",
            shipping_address={
                "city": "San Francisco",
                "country": "United States",
                "line1": "Conductor Labs Inc.",
                "line2": "540 Market St.",
                "line3": "Suite 100",
                "line4": "",
                "line5": "",
                "note": "Conductor HQ",
                "postal_code": "94110",
                "state": "CA",
            },
            shipping_date=parse_date("2024-10-01"),
            shipping_method_id="80000001-1234567890",
            terms_id="80000001-1234567890",
        )
        assert_matches_type(SalesOrder, sales_order, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.sales_orders.with_raw_response.create(
            customer_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sales_order = await response.parse()
        assert_matches_type(SalesOrder, sales_order, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.sales_orders.with_streaming_response.create(
            customer_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sales_order = await response.parse()
            assert_matches_type(SalesOrder, sales_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncConductor) -> None:
        sales_order = await async_client.qbd.sales_orders.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SalesOrder, sales_order, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.sales_orders.with_raw_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sales_order = await response.parse()
        assert_matches_type(SalesOrder, sales_order, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.sales_orders.with_streaming_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sales_order = await response.parse()
            assert_matches_type(SalesOrder, sales_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.sales_orders.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncConductor) -> None:
        sales_order = await async_client.qbd.sales_orders.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SalesOrder, sales_order, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncConductor) -> None:
        sales_order = await async_client.qbd.sales_orders.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
            billing_address={
                "city": "San Francisco",
                "country": "United States",
                "line1": "Conductor Labs Inc.",
                "line2": "540 Market St.",
                "line3": "Suite 100",
                "line4": "",
                "line5": "",
                "note": "Conductor HQ",
                "postal_code": "94110",
                "state": "CA",
            },
            class_id="80000001-1234567890",
            customer_id="80000001-1234567890",
            customer_message_id="80000001-1234567890",
            document_template_id="80000001-1234567890",
            due_date=parse_date("2024-10-31"),
            exchange_rate=1.2345,
            is_manually_closed=True,
            is_queued_for_email=True,
            is_queued_for_print=True,
            line_groups=[
                {
                    "id": "456DEF-1234567890",
                    "item_group_id": "80000001-1234567890",
                    "lines": [
                        {
                            "id": "456DEF-1234567890",
                            "amount": "1000.00",
                            "class_id": "80000001-1234567890",
                            "description": "Widget Model X100 - Blue",
                            "inventory_site_id": "80000001-1234567890",
                            "inventory_site_location_id": "80000001-1234567890",
                            "is_manually_closed": True,
                            "item_id": "80000001-1234567890",
                            "lot_number": "LOT2023-001",
                            "other_custom_field1": "Special handling required",
                            "other_custom_field2": "Always ship with a spare",
                            "override_unit_of_measure_set_id": "80000001-1234567890",
                            "price_level_id": "80000001-1234567890",
                            "price_rule_conflict_strategy": "base_price",
                            "quantity": 5,
                            "rate": "10.00",
                            "rate_percent": "10.5",
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
            lines=[
                {
                    "id": "456DEF-1234567890",
                    "amount": "1000.00",
                    "class_id": "80000001-1234567890",
                    "description": "Widget Model X100 - Blue",
                    "inventory_site_id": "80000001-1234567890",
                    "inventory_site_location_id": "80000001-1234567890",
                    "is_manually_closed": True,
                    "item_id": "80000001-1234567890",
                    "lot_number": "LOT2023-001",
                    "other_custom_field1": "Special handling required",
                    "other_custom_field2": "Always ship with a spare",
                    "override_unit_of_measure_set_id": "80000001-1234567890",
                    "price_level_id": "80000001-1234567890",
                    "price_rule_conflict_strategy": "base_price",
                    "quantity": 5,
                    "rate": "10.00",
                    "rate_percent": "10.5",
                    "sales_tax_code_id": "80000001-1234567890",
                    "serial_number": "SN1234567890",
                    "unit_of_measure": "Each",
                }
            ],
            memo="Customer requested rush delivery",
            other_custom_field="Special handling required",
            purchase_order_number="PO-1234",
            ref_number="SO-1234",
            sales_channel_name="ecommerce",
            sales_representative_id="80000001-1234567890",
            sales_store_name="Store 1",
            sales_store_type="Retail",
            sales_tax_code_id="80000001-1234567890",
            sales_tax_item_id="80000001-1234567890",
            shipment_origin="San Francisco, CA",
            shipping_address={
                "city": "San Francisco",
                "country": "United States",
                "line1": "Conductor Labs Inc.",
                "line2": "540 Market St.",
                "line3": "Suite 100",
                "line4": "",
                "line5": "",
                "note": "Conductor HQ",
                "postal_code": "94110",
                "state": "CA",
            },
            shipping_date=parse_date("2024-10-01"),
            shipping_method_id="80000001-1234567890",
            terms_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
        )
        assert_matches_type(SalesOrder, sales_order, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.sales_orders.with_raw_response.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sales_order = await response.parse()
        assert_matches_type(SalesOrder, sales_order, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.sales_orders.with_streaming_response.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sales_order = await response.parse()
            assert_matches_type(SalesOrder, sales_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.sales_orders.with_raw_response.update(
                id="",
                revision_number="1721172183",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncConductor) -> None:
        sales_order = await async_client.qbd.sales_orders.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(AsyncCursorPage[SalesOrder], sales_order, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncConductor) -> None:
        sales_order = await async_client.qbd.sales_orders.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            currency_ids=["80000001-1234567890"],
            cursor="12345678-abcd-abcd-example-1234567890ab",
            customer_ids=["80000001-1234567890"],
            ids=["123ABC-1234567890"],
            include_line_items=True,
            include_linked_transactions=False,
            limit=150,
            ref_number_contains="SO-1234",
            ref_number_ends_with="1234",
            ref_number_from="SO-0001",
            ref_numbers=["SALES ORDER-1234"],
            ref_number_starts_with="SO",
            ref_number_to="SO-9999",
            transaction_date_from=parse_date("2025-01-01"),
            transaction_date_to=parse_date("2025-02-01"),
            updated_after="2025-01-01T12:34:56+00:00",
            updated_before="2025-02-01T12:34:56+00:00",
        )
        assert_matches_type(AsyncCursorPage[SalesOrder], sales_order, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.sales_orders.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sales_order = await response.parse()
        assert_matches_type(AsyncCursorPage[SalesOrder], sales_order, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.sales_orders.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sales_order = await response.parse()
            assert_matches_type(AsyncCursorPage[SalesOrder], sales_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncConductor) -> None:
        sales_order = await async_client.qbd.sales_orders.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SalesOrderDeleteResponse, sales_order, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.sales_orders.with_raw_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sales_order = await response.parse()
        assert_matches_type(SalesOrderDeleteResponse, sales_order, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.sales_orders.with_streaming_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sales_order = await response.parse()
            assert_matches_type(SalesOrderDeleteResponse, sales_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.sales_orders.with_raw_response.delete(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )
