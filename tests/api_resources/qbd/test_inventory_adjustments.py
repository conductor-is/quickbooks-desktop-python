# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor._utils import parse_date
from conductor.types.qbd import (
    InventoryAdjustment,
    InventoryAdjustmentListResponse,
    InventoryAdjustmentDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInventoryAdjustments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Conductor) -> None:
        inventory_adjustment = client.qbd.inventory_adjustments.create(
            account_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(InventoryAdjustment, inventory_adjustment, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Conductor) -> None:
        inventory_adjustment = client.qbd.inventory_adjustments.create(
            account_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
            class_id="80000001-1234567890",
            customer_id="80000001-1234567890",
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            inventory_site_id="80000001-1234567890",
            lines=[
                {
                    "item_id": "80000001-1234567890",
                    "adjust_lot_number": {
                        "adjust_count": 2,
                        "expiration_date": parse_date("2025-12-31"),
                        "inventory_site_location_id": "80000001-1234567890",
                        "lot_number": "LOT2023-001",
                    },
                    "adjust_quantity": {
                        "expiration_date": parse_date("2025-12-31"),
                        "inventory_site_location_id": "80000001-1234567890",
                        "lot_number": "LOT2023-001",
                        "new_quantity": 10,
                        "quantity_difference": 5,
                        "serial_number": "SN1234567890",
                    },
                    "adjust_serial_number": {
                        "add_serial_number": "123456",
                        "expiration_date": parse_date("2025-12-31"),
                        "inventory_site_location_id": "80000001-1234567890",
                        "remove_serial_number": "123456",
                    },
                    "adjust_value": {
                        "new_quantity": 10,
                        "new_value": "100.00",
                        "quantity_difference": 5,
                        "value_difference": 7,
                    },
                }
            ],
            memo="Adjusted quantity due to physical count discrepancy",
            ref_number="INVADJ-1234",
        )
        assert_matches_type(InventoryAdjustment, inventory_adjustment, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Conductor) -> None:
        response = client.qbd.inventory_adjustments.with_raw_response.create(
            account_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inventory_adjustment = response.parse()
        assert_matches_type(InventoryAdjustment, inventory_adjustment, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Conductor) -> None:
        with client.qbd.inventory_adjustments.with_streaming_response.create(
            account_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inventory_adjustment = response.parse()
            assert_matches_type(InventoryAdjustment, inventory_adjustment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Conductor) -> None:
        inventory_adjustment = client.qbd.inventory_adjustments.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(InventoryAdjustment, inventory_adjustment, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Conductor) -> None:
        response = client.qbd.inventory_adjustments.with_raw_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inventory_adjustment = response.parse()
        assert_matches_type(InventoryAdjustment, inventory_adjustment, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Conductor) -> None:
        with client.qbd.inventory_adjustments.with_streaming_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inventory_adjustment = response.parse()
            assert_matches_type(InventoryAdjustment, inventory_adjustment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.inventory_adjustments.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_update(self, client: Conductor) -> None:
        inventory_adjustment = client.qbd.inventory_adjustments.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(InventoryAdjustment, inventory_adjustment, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Conductor) -> None:
        inventory_adjustment = client.qbd.inventory_adjustments.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_id="80000001-1234567890",
            class_id="80000001-1234567890",
            customer_id="80000001-1234567890",
            inventory_site_id="80000001-1234567890",
            lines=[
                {
                    "id": "456DEF-1234567890",
                    "adjust_count": 2,
                    "expiration_date": parse_date("2025-12-31"),
                    "inventory_site_location_id": "80000001-1234567890",
                    "item_id": "80000001-1234567890",
                    "lot_number": "LOT2023-001",
                    "quantity_difference": 5,
                    "serial_number": "SN1234567890",
                    "value_difference": 7,
                }
            ],
            memo="Adjusted quantity due to physical count discrepancy",
            ref_number="INVADJ-1234",
            transaction_date=parse_date("2024-10-01"),
        )
        assert_matches_type(InventoryAdjustment, inventory_adjustment, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Conductor) -> None:
        response = client.qbd.inventory_adjustments.with_raw_response.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inventory_adjustment = response.parse()
        assert_matches_type(InventoryAdjustment, inventory_adjustment, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Conductor) -> None:
        with client.qbd.inventory_adjustments.with_streaming_response.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inventory_adjustment = response.parse()
            assert_matches_type(InventoryAdjustment, inventory_adjustment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.inventory_adjustments.with_raw_response.update(
                id="",
                revision_number="1721172183",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_list(self, client: Conductor) -> None:
        inventory_adjustment = client.qbd.inventory_adjustments.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(InventoryAdjustmentListResponse, inventory_adjustment, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Conductor) -> None:
        inventory_adjustment = client.qbd.inventory_adjustments.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_ids=["80000001-1234567890"],
            customer_ids=["80000001-1234567890"],
            ids=["123ABC-1234567890"],
            include_line_items=True,
            item_ids=["80000001-1234567890"],
            limit=10,
            ref_number_contains="INVADJ-1234",
            ref_number_ends_with="1234",
            ref_number_from="INVADJ-0001",
            ref_numbers=["INVENTORY ADJUSTMENT-1234"],
            ref_number_starts_with="INVADJ",
            ref_number_to="INVADJ-9999",
            transaction_date_from=parse_date("2025-01-01"),
            transaction_date_to=parse_date("2025-02-01"),
            updated_after="2025-01-01T12:34:56+00:00",
            updated_before="2025-02-01T12:34:56+00:00",
        )
        assert_matches_type(InventoryAdjustmentListResponse, inventory_adjustment, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Conductor) -> None:
        response = client.qbd.inventory_adjustments.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inventory_adjustment = response.parse()
        assert_matches_type(InventoryAdjustmentListResponse, inventory_adjustment, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Conductor) -> None:
        with client.qbd.inventory_adjustments.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inventory_adjustment = response.parse()
            assert_matches_type(InventoryAdjustmentListResponse, inventory_adjustment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Conductor) -> None:
        inventory_adjustment = client.qbd.inventory_adjustments.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(InventoryAdjustmentDeleteResponse, inventory_adjustment, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Conductor) -> None:
        response = client.qbd.inventory_adjustments.with_raw_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inventory_adjustment = response.parse()
        assert_matches_type(InventoryAdjustmentDeleteResponse, inventory_adjustment, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Conductor) -> None:
        with client.qbd.inventory_adjustments.with_streaming_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inventory_adjustment = response.parse()
            assert_matches_type(InventoryAdjustmentDeleteResponse, inventory_adjustment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.inventory_adjustments.with_raw_response.delete(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )


class TestAsyncInventoryAdjustments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncConductor) -> None:
        inventory_adjustment = await async_client.qbd.inventory_adjustments.create(
            account_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(InventoryAdjustment, inventory_adjustment, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncConductor) -> None:
        inventory_adjustment = await async_client.qbd.inventory_adjustments.create(
            account_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
            class_id="80000001-1234567890",
            customer_id="80000001-1234567890",
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            inventory_site_id="80000001-1234567890",
            lines=[
                {
                    "item_id": "80000001-1234567890",
                    "adjust_lot_number": {
                        "adjust_count": 2,
                        "expiration_date": parse_date("2025-12-31"),
                        "inventory_site_location_id": "80000001-1234567890",
                        "lot_number": "LOT2023-001",
                    },
                    "adjust_quantity": {
                        "expiration_date": parse_date("2025-12-31"),
                        "inventory_site_location_id": "80000001-1234567890",
                        "lot_number": "LOT2023-001",
                        "new_quantity": 10,
                        "quantity_difference": 5,
                        "serial_number": "SN1234567890",
                    },
                    "adjust_serial_number": {
                        "add_serial_number": "123456",
                        "expiration_date": parse_date("2025-12-31"),
                        "inventory_site_location_id": "80000001-1234567890",
                        "remove_serial_number": "123456",
                    },
                    "adjust_value": {
                        "new_quantity": 10,
                        "new_value": "100.00",
                        "quantity_difference": 5,
                        "value_difference": 7,
                    },
                }
            ],
            memo="Adjusted quantity due to physical count discrepancy",
            ref_number="INVADJ-1234",
        )
        assert_matches_type(InventoryAdjustment, inventory_adjustment, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.inventory_adjustments.with_raw_response.create(
            account_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inventory_adjustment = await response.parse()
        assert_matches_type(InventoryAdjustment, inventory_adjustment, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.inventory_adjustments.with_streaming_response.create(
            account_id="80000001-1234567890",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inventory_adjustment = await response.parse()
            assert_matches_type(InventoryAdjustment, inventory_adjustment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncConductor) -> None:
        inventory_adjustment = await async_client.qbd.inventory_adjustments.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(InventoryAdjustment, inventory_adjustment, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.inventory_adjustments.with_raw_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inventory_adjustment = await response.parse()
        assert_matches_type(InventoryAdjustment, inventory_adjustment, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.inventory_adjustments.with_streaming_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inventory_adjustment = await response.parse()
            assert_matches_type(InventoryAdjustment, inventory_adjustment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.inventory_adjustments.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncConductor) -> None:
        inventory_adjustment = await async_client.qbd.inventory_adjustments.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(InventoryAdjustment, inventory_adjustment, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncConductor) -> None:
        inventory_adjustment = await async_client.qbd.inventory_adjustments.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_id="80000001-1234567890",
            class_id="80000001-1234567890",
            customer_id="80000001-1234567890",
            inventory_site_id="80000001-1234567890",
            lines=[
                {
                    "id": "456DEF-1234567890",
                    "adjust_count": 2,
                    "expiration_date": parse_date("2025-12-31"),
                    "inventory_site_location_id": "80000001-1234567890",
                    "item_id": "80000001-1234567890",
                    "lot_number": "LOT2023-001",
                    "quantity_difference": 5,
                    "serial_number": "SN1234567890",
                    "value_difference": 7,
                }
            ],
            memo="Adjusted quantity due to physical count discrepancy",
            ref_number="INVADJ-1234",
            transaction_date=parse_date("2024-10-01"),
        )
        assert_matches_type(InventoryAdjustment, inventory_adjustment, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.inventory_adjustments.with_raw_response.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inventory_adjustment = await response.parse()
        assert_matches_type(InventoryAdjustment, inventory_adjustment, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.inventory_adjustments.with_streaming_response.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inventory_adjustment = await response.parse()
            assert_matches_type(InventoryAdjustment, inventory_adjustment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.inventory_adjustments.with_raw_response.update(
                id="",
                revision_number="1721172183",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncConductor) -> None:
        inventory_adjustment = await async_client.qbd.inventory_adjustments.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(InventoryAdjustmentListResponse, inventory_adjustment, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncConductor) -> None:
        inventory_adjustment = await async_client.qbd.inventory_adjustments.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_ids=["80000001-1234567890"],
            customer_ids=["80000001-1234567890"],
            ids=["123ABC-1234567890"],
            include_line_items=True,
            item_ids=["80000001-1234567890"],
            limit=10,
            ref_number_contains="INVADJ-1234",
            ref_number_ends_with="1234",
            ref_number_from="INVADJ-0001",
            ref_numbers=["INVENTORY ADJUSTMENT-1234"],
            ref_number_starts_with="INVADJ",
            ref_number_to="INVADJ-9999",
            transaction_date_from=parse_date("2025-01-01"),
            transaction_date_to=parse_date("2025-02-01"),
            updated_after="2025-01-01T12:34:56+00:00",
            updated_before="2025-02-01T12:34:56+00:00",
        )
        assert_matches_type(InventoryAdjustmentListResponse, inventory_adjustment, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.inventory_adjustments.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inventory_adjustment = await response.parse()
        assert_matches_type(InventoryAdjustmentListResponse, inventory_adjustment, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.inventory_adjustments.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inventory_adjustment = await response.parse()
            assert_matches_type(InventoryAdjustmentListResponse, inventory_adjustment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncConductor) -> None:
        inventory_adjustment = await async_client.qbd.inventory_adjustments.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(InventoryAdjustmentDeleteResponse, inventory_adjustment, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.inventory_adjustments.with_raw_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inventory_adjustment = await response.parse()
        assert_matches_type(InventoryAdjustmentDeleteResponse, inventory_adjustment, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.inventory_adjustments.with_streaming_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inventory_adjustment = await response.parse()
            assert_matches_type(InventoryAdjustmentDeleteResponse, inventory_adjustment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.inventory_adjustments.with_raw_response.delete(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )
