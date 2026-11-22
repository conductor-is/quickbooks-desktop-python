# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor.types.qbd import (
    CustomFieldDefinition,
    CustomFieldDefinitionListResponse,
    CustomFieldDefinitionDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomFieldDefinitions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Conductor) -> None:
        custom_field_definition = client.qbd.custom_field_definitions.create(
            name="Customer Rating",
            object_types=["customer"],
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(CustomFieldDefinition, custom_field_definition, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Conductor) -> None:
        custom_field_definition = client.qbd.custom_field_definitions.create(
            name="Customer Rating",
            object_types=["customer"],
            conductor_end_user_id="end_usr_1234567abcdefg",
            owner_id="0",
            type="string_255_type",
        )
        assert_matches_type(CustomFieldDefinition, custom_field_definition, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Conductor) -> None:
        response = client.qbd.custom_field_definitions.with_raw_response.create(
            name="Customer Rating",
            object_types=["customer"],
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_field_definition = response.parse()
        assert_matches_type(CustomFieldDefinition, custom_field_definition, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Conductor) -> None:
        with client.qbd.custom_field_definitions.with_streaming_response.create(
            name="Customer Rating",
            object_types=["customer"],
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_field_definition = response.parse()
            assert_matches_type(CustomFieldDefinition, custom_field_definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Conductor) -> None:
        custom_field_definition = client.qbd.custom_field_definitions.update(
            id="Customer Rating",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(CustomFieldDefinition, custom_field_definition, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Conductor) -> None:
        custom_field_definition = client.qbd.custom_field_definitions.update(
            id="Customer Rating",
            conductor_end_user_id="end_usr_1234567abcdefg",
            add_object_types=["vendor"],
            name="Customer Tier",
            owner_id="0",
            remove_object_types=["employee"],
        )
        assert_matches_type(CustomFieldDefinition, custom_field_definition, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Conductor) -> None:
        response = client.qbd.custom_field_definitions.with_raw_response.update(
            id="Customer Rating",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_field_definition = response.parse()
        assert_matches_type(CustomFieldDefinition, custom_field_definition, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Conductor) -> None:
        with client.qbd.custom_field_definitions.with_streaming_response.update(
            id="Customer Rating",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_field_definition = response.parse()
            assert_matches_type(CustomFieldDefinition, custom_field_definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.custom_field_definitions.with_raw_response.update(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_list(self, client: Conductor) -> None:
        custom_field_definition = client.qbd.custom_field_definitions.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(CustomFieldDefinitionListResponse, custom_field_definition, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Conductor) -> None:
        custom_field_definition = client.qbd.custom_field_definitions.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            owner_ids=["0"],
        )
        assert_matches_type(CustomFieldDefinitionListResponse, custom_field_definition, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Conductor) -> None:
        response = client.qbd.custom_field_definitions.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_field_definition = response.parse()
        assert_matches_type(CustomFieldDefinitionListResponse, custom_field_definition, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Conductor) -> None:
        with client.qbd.custom_field_definitions.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_field_definition = response.parse()
            assert_matches_type(CustomFieldDefinitionListResponse, custom_field_definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Conductor) -> None:
        custom_field_definition = client.qbd.custom_field_definitions.delete(
            id="Customer Rating",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(CustomFieldDefinitionDeleteResponse, custom_field_definition, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Conductor) -> None:
        custom_field_definition = client.qbd.custom_field_definitions.delete(
            id="Customer Rating",
            conductor_end_user_id="end_usr_1234567abcdefg",
            owner_id="0",
        )
        assert_matches_type(CustomFieldDefinitionDeleteResponse, custom_field_definition, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Conductor) -> None:
        response = client.qbd.custom_field_definitions.with_raw_response.delete(
            id="Customer Rating",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_field_definition = response.parse()
        assert_matches_type(CustomFieldDefinitionDeleteResponse, custom_field_definition, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Conductor) -> None:
        with client.qbd.custom_field_definitions.with_streaming_response.delete(
            id="Customer Rating",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_field_definition = response.parse()
            assert_matches_type(CustomFieldDefinitionDeleteResponse, custom_field_definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.custom_field_definitions.with_raw_response.delete(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )


class TestAsyncCustomFieldDefinitions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncConductor) -> None:
        custom_field_definition = await async_client.qbd.custom_field_definitions.create(
            name="Customer Rating",
            object_types=["customer"],
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(CustomFieldDefinition, custom_field_definition, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncConductor) -> None:
        custom_field_definition = await async_client.qbd.custom_field_definitions.create(
            name="Customer Rating",
            object_types=["customer"],
            conductor_end_user_id="end_usr_1234567abcdefg",
            owner_id="0",
            type="string_255_type",
        )
        assert_matches_type(CustomFieldDefinition, custom_field_definition, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.custom_field_definitions.with_raw_response.create(
            name="Customer Rating",
            object_types=["customer"],
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_field_definition = await response.parse()
        assert_matches_type(CustomFieldDefinition, custom_field_definition, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.custom_field_definitions.with_streaming_response.create(
            name="Customer Rating",
            object_types=["customer"],
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_field_definition = await response.parse()
            assert_matches_type(CustomFieldDefinition, custom_field_definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncConductor) -> None:
        custom_field_definition = await async_client.qbd.custom_field_definitions.update(
            id="Customer Rating",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(CustomFieldDefinition, custom_field_definition, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncConductor) -> None:
        custom_field_definition = await async_client.qbd.custom_field_definitions.update(
            id="Customer Rating",
            conductor_end_user_id="end_usr_1234567abcdefg",
            add_object_types=["vendor"],
            name="Customer Tier",
            owner_id="0",
            remove_object_types=["employee"],
        )
        assert_matches_type(CustomFieldDefinition, custom_field_definition, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.custom_field_definitions.with_raw_response.update(
            id="Customer Rating",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_field_definition = await response.parse()
        assert_matches_type(CustomFieldDefinition, custom_field_definition, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.custom_field_definitions.with_streaming_response.update(
            id="Customer Rating",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_field_definition = await response.parse()
            assert_matches_type(CustomFieldDefinition, custom_field_definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.custom_field_definitions.with_raw_response.update(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncConductor) -> None:
        custom_field_definition = await async_client.qbd.custom_field_definitions.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(CustomFieldDefinitionListResponse, custom_field_definition, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncConductor) -> None:
        custom_field_definition = await async_client.qbd.custom_field_definitions.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            owner_ids=["0"],
        )
        assert_matches_type(CustomFieldDefinitionListResponse, custom_field_definition, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.custom_field_definitions.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_field_definition = await response.parse()
        assert_matches_type(CustomFieldDefinitionListResponse, custom_field_definition, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.custom_field_definitions.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_field_definition = await response.parse()
            assert_matches_type(CustomFieldDefinitionListResponse, custom_field_definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncConductor) -> None:
        custom_field_definition = await async_client.qbd.custom_field_definitions.delete(
            id="Customer Rating",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(CustomFieldDefinitionDeleteResponse, custom_field_definition, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncConductor) -> None:
        custom_field_definition = await async_client.qbd.custom_field_definitions.delete(
            id="Customer Rating",
            conductor_end_user_id="end_usr_1234567abcdefg",
            owner_id="0",
        )
        assert_matches_type(CustomFieldDefinitionDeleteResponse, custom_field_definition, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.custom_field_definitions.with_raw_response.delete(
            id="Customer Rating",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_field_definition = await response.parse()
        assert_matches_type(CustomFieldDefinitionDeleteResponse, custom_field_definition, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.custom_field_definitions.with_streaming_response.delete(
            id="Customer Rating",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_field_definition = await response.parse()
            assert_matches_type(CustomFieldDefinitionDeleteResponse, custom_field_definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.custom_field_definitions.with_raw_response.delete(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )
