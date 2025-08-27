# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor.types.qbd import (
    InventorySite,
    InventorySiteListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInventorySites:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Conductor) -> None:
        inventory_site = client.qbd.inventory_sites.create(
            name="Stockroom",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(InventorySite, inventory_site, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Conductor) -> None:
        inventory_site = client.qbd.inventory_sites.create(
            name="Stockroom",
            conductor_end_user_id="end_usr_1234567abcdefg",
            address={
                "city": "San Francisco",
                "country": "United States",
                "line1": "Conductor Labs Inc.",
                "line2": "540 Market St.",
                "line3": "Suite 100",
                "line4": "",
                "line5": "",
                "postal_code": "94110",
                "state": "CA",
            },
            description="Main Stockroom for Electronics",
            email="inventory-site@example.com",
            is_active=True,
            parent_id="80000001-1234567890",
        )
        assert_matches_type(InventorySite, inventory_site, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Conductor) -> None:
        response = client.qbd.inventory_sites.with_raw_response.create(
            name="Stockroom",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inventory_site = response.parse()
        assert_matches_type(InventorySite, inventory_site, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Conductor) -> None:
        with client.qbd.inventory_sites.with_streaming_response.create(
            name="Stockroom",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inventory_site = response.parse()
            assert_matches_type(InventorySite, inventory_site, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Conductor) -> None:
        inventory_site = client.qbd.inventory_sites.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(InventorySite, inventory_site, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Conductor) -> None:
        response = client.qbd.inventory_sites.with_raw_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inventory_site = response.parse()
        assert_matches_type(InventorySite, inventory_site, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Conductor) -> None:
        with client.qbd.inventory_sites.with_streaming_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inventory_site = response.parse()
            assert_matches_type(InventorySite, inventory_site, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.inventory_sites.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_update(self, client: Conductor) -> None:
        inventory_site = client.qbd.inventory_sites.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(InventorySite, inventory_site, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Conductor) -> None:
        inventory_site = client.qbd.inventory_sites.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
            address={
                "city": "San Francisco",
                "country": "United States",
                "line1": "Conductor Labs Inc.",
                "line2": "540 Market St.",
                "line3": "Suite 100",
                "line4": "",
                "line5": "",
                "postal_code": "94110",
                "state": "CA",
            },
            contact="Jane Smith",
            description="Main Stockroom for Electronics",
            email="inventory-site@example.com",
            fax="+1-555-555-1212",
            is_active=True,
            name="Stockroom",
            parent_id="80000001-1234567890",
            phone="+1-555-123-4567",
        )
        assert_matches_type(InventorySite, inventory_site, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Conductor) -> None:
        response = client.qbd.inventory_sites.with_raw_response.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inventory_site = response.parse()
        assert_matches_type(InventorySite, inventory_site, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Conductor) -> None:
        with client.qbd.inventory_sites.with_streaming_response.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inventory_site = response.parse()
            assert_matches_type(InventorySite, inventory_site, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.inventory_sites.with_raw_response.update(
                id="",
                revision_number="1721172183",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_list(self, client: Conductor) -> None:
        inventory_site = client.qbd.inventory_sites.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(InventorySiteListResponse, inventory_site, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Conductor) -> None:
        inventory_site = client.qbd.inventory_sites.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            ids=["80000001-1234567890"],
            name_contains="ABC",
            name_ends_with="ABC",
            name_from="A",
            names=["Stockroom"],
            name_starts_with="ABC",
            name_to="Z",
            status="active",
            updated_after="2025-01-01T12:34:56+00:00",
            updated_before="2025-02-01T12:34:56+00:00",
        )
        assert_matches_type(InventorySiteListResponse, inventory_site, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Conductor) -> None:
        response = client.qbd.inventory_sites.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inventory_site = response.parse()
        assert_matches_type(InventorySiteListResponse, inventory_site, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Conductor) -> None:
        with client.qbd.inventory_sites.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inventory_site = response.parse()
            assert_matches_type(InventorySiteListResponse, inventory_site, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInventorySites:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncConductor) -> None:
        inventory_site = await async_client.qbd.inventory_sites.create(
            name="Stockroom",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(InventorySite, inventory_site, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncConductor) -> None:
        inventory_site = await async_client.qbd.inventory_sites.create(
            name="Stockroom",
            conductor_end_user_id="end_usr_1234567abcdefg",
            address={
                "city": "San Francisco",
                "country": "United States",
                "line1": "Conductor Labs Inc.",
                "line2": "540 Market St.",
                "line3": "Suite 100",
                "line4": "",
                "line5": "",
                "postal_code": "94110",
                "state": "CA",
            },
            description="Main Stockroom for Electronics",
            email="inventory-site@example.com",
            is_active=True,
            parent_id="80000001-1234567890",
        )
        assert_matches_type(InventorySite, inventory_site, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.inventory_sites.with_raw_response.create(
            name="Stockroom",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inventory_site = await response.parse()
        assert_matches_type(InventorySite, inventory_site, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.inventory_sites.with_streaming_response.create(
            name="Stockroom",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inventory_site = await response.parse()
            assert_matches_type(InventorySite, inventory_site, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncConductor) -> None:
        inventory_site = await async_client.qbd.inventory_sites.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(InventorySite, inventory_site, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.inventory_sites.with_raw_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inventory_site = await response.parse()
        assert_matches_type(InventorySite, inventory_site, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.inventory_sites.with_streaming_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inventory_site = await response.parse()
            assert_matches_type(InventorySite, inventory_site, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.inventory_sites.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncConductor) -> None:
        inventory_site = await async_client.qbd.inventory_sites.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(InventorySite, inventory_site, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncConductor) -> None:
        inventory_site = await async_client.qbd.inventory_sites.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
            address={
                "city": "San Francisco",
                "country": "United States",
                "line1": "Conductor Labs Inc.",
                "line2": "540 Market St.",
                "line3": "Suite 100",
                "line4": "",
                "line5": "",
                "postal_code": "94110",
                "state": "CA",
            },
            contact="Jane Smith",
            description="Main Stockroom for Electronics",
            email="inventory-site@example.com",
            fax="+1-555-555-1212",
            is_active=True,
            name="Stockroom",
            parent_id="80000001-1234567890",
            phone="+1-555-123-4567",
        )
        assert_matches_type(InventorySite, inventory_site, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.inventory_sites.with_raw_response.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inventory_site = await response.parse()
        assert_matches_type(InventorySite, inventory_site, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.inventory_sites.with_streaming_response.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inventory_site = await response.parse()
            assert_matches_type(InventorySite, inventory_site, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.inventory_sites.with_raw_response.update(
                id="",
                revision_number="1721172183",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncConductor) -> None:
        inventory_site = await async_client.qbd.inventory_sites.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(InventorySiteListResponse, inventory_site, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncConductor) -> None:
        inventory_site = await async_client.qbd.inventory_sites.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            ids=["80000001-1234567890"],
            name_contains="ABC",
            name_ends_with="ABC",
            name_from="A",
            names=["Stockroom"],
            name_starts_with="ABC",
            name_to="Z",
            status="active",
            updated_after="2025-01-01T12:34:56+00:00",
            updated_before="2025-02-01T12:34:56+00:00",
        )
        assert_matches_type(InventorySiteListResponse, inventory_site, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.inventory_sites.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inventory_site = await response.parse()
        assert_matches_type(InventorySiteListResponse, inventory_site, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.inventory_sites.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inventory_site = await response.parse()
            assert_matches_type(InventorySiteListResponse, inventory_site, path=["response"])

        assert cast(Any, response.is_closed) is True
