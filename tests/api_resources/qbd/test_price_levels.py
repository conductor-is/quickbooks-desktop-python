# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor.types.qbd import (
    PriceLevel,
    PriceLevelListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPriceLevels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Conductor) -> None:
        price_level = client.qbd.price_levels.create(
            name="Wholesale 20% Discount",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(PriceLevel, price_level, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Conductor) -> None:
        price_level = client.qbd.price_levels.create(
            name="Wholesale 20% Discount",
            conductor_end_user_id="end_usr_1234567abcdefg",
            currency_id="80000001-1234567890",
            fixed_percentage="-10.0",
            is_active=True,
            per_item_price_levels=[
                {
                    "adjust_percentage": "-10.0",
                    "adjust_relative_to": "standard_price",
                    "item_id": "80000001-1234567890",
                    "custom_price": "19.99",
                    "custom_price_percent": "15.0",
                }
            ],
        )
        assert_matches_type(PriceLevel, price_level, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Conductor) -> None:
        response = client.qbd.price_levels.with_raw_response.create(
            name="Wholesale 20% Discount",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price_level = response.parse()
        assert_matches_type(PriceLevel, price_level, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Conductor) -> None:
        with client.qbd.price_levels.with_streaming_response.create(
            name="Wholesale 20% Discount",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price_level = response.parse()
            assert_matches_type(PriceLevel, price_level, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Conductor) -> None:
        price_level = client.qbd.price_levels.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(PriceLevel, price_level, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Conductor) -> None:
        response = client.qbd.price_levels.with_raw_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price_level = response.parse()
        assert_matches_type(PriceLevel, price_level, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Conductor) -> None:
        with client.qbd.price_levels.with_streaming_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price_level = response.parse()
            assert_matches_type(PriceLevel, price_level, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.price_levels.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_update(self, client: Conductor) -> None:
        price_level = client.qbd.price_levels.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(PriceLevel, price_level, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Conductor) -> None:
        price_level = client.qbd.price_levels.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
            currency_id="80000001-1234567890",
            fixed_percentage="-10.0",
            is_active=True,
            name="Wholesale 20% Discount",
            per_item_price_levels=[
                {
                    "adjust_percentage": "-10.0",
                    "adjust_relative_to": "standard_price",
                    "item_id": "80000001-1234567890",
                    "custom_price": "19.99",
                    "custom_price_percent": "15.0",
                }
            ],
        )
        assert_matches_type(PriceLevel, price_level, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Conductor) -> None:
        response = client.qbd.price_levels.with_raw_response.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price_level = response.parse()
        assert_matches_type(PriceLevel, price_level, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Conductor) -> None:
        with client.qbd.price_levels.with_streaming_response.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price_level = response.parse()
            assert_matches_type(PriceLevel, price_level, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.price_levels.with_raw_response.update(
                id="",
                revision_number="1721172183",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_list(self, client: Conductor) -> None:
        price_level = client.qbd.price_levels.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(PriceLevelListResponse, price_level, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Conductor) -> None:
        price_level = client.qbd.price_levels.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            currency_ids=["80000001-1234567890"],
            ids=["80000001-1234567890"],
            item_ids=["80000001-1234567890"],
            limit=10,
            name_contains="ABC",
            name_ends_with="ABC",
            name_from="A",
            names=["Wholesale 20% Discount"],
            name_starts_with="ABC",
            name_to="Z",
            status="active",
            updated_after="2025-01-01T12:34:56+00:00",
            updated_before="2025-02-01T12:34:56+00:00",
        )
        assert_matches_type(PriceLevelListResponse, price_level, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Conductor) -> None:
        response = client.qbd.price_levels.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price_level = response.parse()
        assert_matches_type(PriceLevelListResponse, price_level, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Conductor) -> None:
        with client.qbd.price_levels.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price_level = response.parse()
            assert_matches_type(PriceLevelListResponse, price_level, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPriceLevels:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncConductor) -> None:
        price_level = await async_client.qbd.price_levels.create(
            name="Wholesale 20% Discount",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(PriceLevel, price_level, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncConductor) -> None:
        price_level = await async_client.qbd.price_levels.create(
            name="Wholesale 20% Discount",
            conductor_end_user_id="end_usr_1234567abcdefg",
            currency_id="80000001-1234567890",
            fixed_percentage="-10.0",
            is_active=True,
            per_item_price_levels=[
                {
                    "adjust_percentage": "-10.0",
                    "adjust_relative_to": "standard_price",
                    "item_id": "80000001-1234567890",
                    "custom_price": "19.99",
                    "custom_price_percent": "15.0",
                }
            ],
        )
        assert_matches_type(PriceLevel, price_level, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.price_levels.with_raw_response.create(
            name="Wholesale 20% Discount",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price_level = await response.parse()
        assert_matches_type(PriceLevel, price_level, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.price_levels.with_streaming_response.create(
            name="Wholesale 20% Discount",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price_level = await response.parse()
            assert_matches_type(PriceLevel, price_level, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncConductor) -> None:
        price_level = await async_client.qbd.price_levels.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(PriceLevel, price_level, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.price_levels.with_raw_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price_level = await response.parse()
        assert_matches_type(PriceLevel, price_level, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.price_levels.with_streaming_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price_level = await response.parse()
            assert_matches_type(PriceLevel, price_level, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.price_levels.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncConductor) -> None:
        price_level = await async_client.qbd.price_levels.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(PriceLevel, price_level, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncConductor) -> None:
        price_level = await async_client.qbd.price_levels.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
            currency_id="80000001-1234567890",
            fixed_percentage="-10.0",
            is_active=True,
            name="Wholesale 20% Discount",
            per_item_price_levels=[
                {
                    "adjust_percentage": "-10.0",
                    "adjust_relative_to": "standard_price",
                    "item_id": "80000001-1234567890",
                    "custom_price": "19.99",
                    "custom_price_percent": "15.0",
                }
            ],
        )
        assert_matches_type(PriceLevel, price_level, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.price_levels.with_raw_response.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price_level = await response.parse()
        assert_matches_type(PriceLevel, price_level, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.price_levels.with_streaming_response.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price_level = await response.parse()
            assert_matches_type(PriceLevel, price_level, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.price_levels.with_raw_response.update(
                id="",
                revision_number="1721172183",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncConductor) -> None:
        price_level = await async_client.qbd.price_levels.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(PriceLevelListResponse, price_level, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncConductor) -> None:
        price_level = await async_client.qbd.price_levels.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            currency_ids=["80000001-1234567890"],
            ids=["80000001-1234567890"],
            item_ids=["80000001-1234567890"],
            limit=10,
            name_contains="ABC",
            name_ends_with="ABC",
            name_from="A",
            names=["Wholesale 20% Discount"],
            name_starts_with="ABC",
            name_to="Z",
            status="active",
            updated_after="2025-01-01T12:34:56+00:00",
            updated_before="2025-02-01T12:34:56+00:00",
        )
        assert_matches_type(PriceLevelListResponse, price_level, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.price_levels.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price_level = await response.parse()
        assert_matches_type(PriceLevelListResponse, price_level, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.price_levels.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price_level = await response.parse()
            assert_matches_type(PriceLevelListResponse, price_level, path=["response"])

        assert cast(Any, response.is_closed) is True
