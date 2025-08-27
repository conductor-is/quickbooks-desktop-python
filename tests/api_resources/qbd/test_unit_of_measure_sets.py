# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor.types.qbd import (
    UnitOfMeasureSet,
    UnitOfMeasureSetListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUnitOfMeasureSets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Conductor) -> None:
        unit_of_measure_set = client.qbd.unit_of_measure_sets.create(
            base_unit={
                "abbreviation": "ea",
                "name": "Each",
            },
            name="Weight Units",
            unit_of_measure_type="count",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(UnitOfMeasureSet, unit_of_measure_set, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Conductor) -> None:
        unit_of_measure_set = client.qbd.unit_of_measure_sets.create(
            base_unit={
                "abbreviation": "ea",
                "name": "Each",
            },
            name="Weight Units",
            unit_of_measure_type="count",
            conductor_end_user_id="end_usr_1234567abcdefg",
            default_units=[
                {
                    "unit": "Each",
                    "unit_used_for": "purchase",
                }
            ],
            is_active=True,
            related_units=[
                {
                    "abbreviation": "ea",
                    "conversion_ratio": "10",
                    "name": "Case",
                }
            ],
        )
        assert_matches_type(UnitOfMeasureSet, unit_of_measure_set, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Conductor) -> None:
        response = client.qbd.unit_of_measure_sets.with_raw_response.create(
            base_unit={
                "abbreviation": "ea",
                "name": "Each",
            },
            name="Weight Units",
            unit_of_measure_type="count",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        unit_of_measure_set = response.parse()
        assert_matches_type(UnitOfMeasureSet, unit_of_measure_set, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Conductor) -> None:
        with client.qbd.unit_of_measure_sets.with_streaming_response.create(
            base_unit={
                "abbreviation": "ea",
                "name": "Each",
            },
            name="Weight Units",
            unit_of_measure_type="count",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            unit_of_measure_set = response.parse()
            assert_matches_type(UnitOfMeasureSet, unit_of_measure_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Conductor) -> None:
        unit_of_measure_set = client.qbd.unit_of_measure_sets.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(UnitOfMeasureSet, unit_of_measure_set, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Conductor) -> None:
        response = client.qbd.unit_of_measure_sets.with_raw_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        unit_of_measure_set = response.parse()
        assert_matches_type(UnitOfMeasureSet, unit_of_measure_set, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Conductor) -> None:
        with client.qbd.unit_of_measure_sets.with_streaming_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            unit_of_measure_set = response.parse()
            assert_matches_type(UnitOfMeasureSet, unit_of_measure_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.unit_of_measure_sets.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_list(self, client: Conductor) -> None:
        unit_of_measure_set = client.qbd.unit_of_measure_sets.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(UnitOfMeasureSetListResponse, unit_of_measure_set, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Conductor) -> None:
        unit_of_measure_set = client.qbd.unit_of_measure_sets.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            ids=["80000001-1234567890"],
            limit=10,
            name_contains="ABC",
            name_ends_with="ABC",
            name_from="A",
            names=["Weight Units"],
            name_starts_with="ABC",
            name_to="Z",
            status="active",
            updated_after="2025-01-01T12:34:56+00:00",
            updated_before="2025-02-01T12:34:56+00:00",
        )
        assert_matches_type(UnitOfMeasureSetListResponse, unit_of_measure_set, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Conductor) -> None:
        response = client.qbd.unit_of_measure_sets.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        unit_of_measure_set = response.parse()
        assert_matches_type(UnitOfMeasureSetListResponse, unit_of_measure_set, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Conductor) -> None:
        with client.qbd.unit_of_measure_sets.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            unit_of_measure_set = response.parse()
            assert_matches_type(UnitOfMeasureSetListResponse, unit_of_measure_set, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUnitOfMeasureSets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncConductor) -> None:
        unit_of_measure_set = await async_client.qbd.unit_of_measure_sets.create(
            base_unit={
                "abbreviation": "ea",
                "name": "Each",
            },
            name="Weight Units",
            unit_of_measure_type="count",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(UnitOfMeasureSet, unit_of_measure_set, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncConductor) -> None:
        unit_of_measure_set = await async_client.qbd.unit_of_measure_sets.create(
            base_unit={
                "abbreviation": "ea",
                "name": "Each",
            },
            name="Weight Units",
            unit_of_measure_type="count",
            conductor_end_user_id="end_usr_1234567abcdefg",
            default_units=[
                {
                    "unit": "Each",
                    "unit_used_for": "purchase",
                }
            ],
            is_active=True,
            related_units=[
                {
                    "abbreviation": "ea",
                    "conversion_ratio": "10",
                    "name": "Case",
                }
            ],
        )
        assert_matches_type(UnitOfMeasureSet, unit_of_measure_set, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.unit_of_measure_sets.with_raw_response.create(
            base_unit={
                "abbreviation": "ea",
                "name": "Each",
            },
            name="Weight Units",
            unit_of_measure_type="count",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        unit_of_measure_set = await response.parse()
        assert_matches_type(UnitOfMeasureSet, unit_of_measure_set, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.unit_of_measure_sets.with_streaming_response.create(
            base_unit={
                "abbreviation": "ea",
                "name": "Each",
            },
            name="Weight Units",
            unit_of_measure_type="count",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            unit_of_measure_set = await response.parse()
            assert_matches_type(UnitOfMeasureSet, unit_of_measure_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncConductor) -> None:
        unit_of_measure_set = await async_client.qbd.unit_of_measure_sets.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(UnitOfMeasureSet, unit_of_measure_set, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.unit_of_measure_sets.with_raw_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        unit_of_measure_set = await response.parse()
        assert_matches_type(UnitOfMeasureSet, unit_of_measure_set, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.unit_of_measure_sets.with_streaming_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            unit_of_measure_set = await response.parse()
            assert_matches_type(UnitOfMeasureSet, unit_of_measure_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.unit_of_measure_sets.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncConductor) -> None:
        unit_of_measure_set = await async_client.qbd.unit_of_measure_sets.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(UnitOfMeasureSetListResponse, unit_of_measure_set, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncConductor) -> None:
        unit_of_measure_set = await async_client.qbd.unit_of_measure_sets.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            ids=["80000001-1234567890"],
            limit=10,
            name_contains="ABC",
            name_ends_with="ABC",
            name_from="A",
            names=["Weight Units"],
            name_starts_with="ABC",
            name_to="Z",
            status="active",
            updated_after="2025-01-01T12:34:56+00:00",
            updated_before="2025-02-01T12:34:56+00:00",
        )
        assert_matches_type(UnitOfMeasureSetListResponse, unit_of_measure_set, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.unit_of_measure_sets.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        unit_of_measure_set = await response.parse()
        assert_matches_type(UnitOfMeasureSetListResponse, unit_of_measure_set, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.unit_of_measure_sets.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            unit_of_measure_set = await response.parse()
            assert_matches_type(UnitOfMeasureSetListResponse, unit_of_measure_set, path=["response"])

        assert cast(Any, response.is_closed) is True
