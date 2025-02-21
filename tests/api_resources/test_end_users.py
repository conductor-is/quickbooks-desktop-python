# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor.types import (
    EndUser,
    EndUserListResponse,
    EndUserPingResponse,
    EndUserDeleteResponse,
    EndUserPassthroughResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEndUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Conductor) -> None:
        end_user = client.end_users.create(
            company_name="Acme Inc.",
            email="alice@acme.com",
            source_id="12345678-abcd-abcd-example-1234567890ab",
        )
        assert_matches_type(EndUser, end_user, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Conductor) -> None:
        response = client.end_users.with_raw_response.create(
            company_name="Acme Inc.",
            email="alice@acme.com",
            source_id="12345678-abcd-abcd-example-1234567890ab",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        end_user = response.parse()
        assert_matches_type(EndUser, end_user, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Conductor) -> None:
        with client.end_users.with_streaming_response.create(
            company_name="Acme Inc.",
            email="alice@acme.com",
            source_id="12345678-abcd-abcd-example-1234567890ab",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            end_user = response.parse()
            assert_matches_type(EndUser, end_user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Conductor) -> None:
        end_user = client.end_users.retrieve(
            "end_usr_1234567abcdefg",
        )
        assert_matches_type(EndUser, end_user, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Conductor) -> None:
        response = client.end_users.with_raw_response.retrieve(
            "end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        end_user = response.parse()
        assert_matches_type(EndUser, end_user, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Conductor) -> None:
        with client.end_users.with_streaming_response.retrieve(
            "end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            end_user = response.parse()
            assert_matches_type(EndUser, end_user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.end_users.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Conductor) -> None:
        end_user = client.end_users.list()
        assert_matches_type(EndUserListResponse, end_user, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Conductor) -> None:
        response = client.end_users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        end_user = response.parse()
        assert_matches_type(EndUserListResponse, end_user, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Conductor) -> None:
        with client.end_users.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            end_user = response.parse()
            assert_matches_type(EndUserListResponse, end_user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Conductor) -> None:
        end_user = client.end_users.delete(
            "end_usr_1234567abcdefg",
        )
        assert_matches_type(EndUserDeleteResponse, end_user, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Conductor) -> None:
        response = client.end_users.with_raw_response.delete(
            "end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        end_user = response.parse()
        assert_matches_type(EndUserDeleteResponse, end_user, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Conductor) -> None:
        with client.end_users.with_streaming_response.delete(
            "end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            end_user = response.parse()
            assert_matches_type(EndUserDeleteResponse, end_user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.end_users.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_passthrough(self, client: Conductor) -> None:
        end_user = client.end_users.passthrough(
            integration_slug="quickbooks_desktop",
            id="end_usr_1234567abcdefg",
            qbd_payload={"foo": "bar"},
        )
        assert_matches_type(EndUserPassthroughResponse, end_user, path=["response"])

    @parametrize
    def test_raw_response_passthrough(self, client: Conductor) -> None:
        response = client.end_users.with_raw_response.passthrough(
            integration_slug="quickbooks_desktop",
            id="end_usr_1234567abcdefg",
            qbd_payload={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        end_user = response.parse()
        assert_matches_type(EndUserPassthroughResponse, end_user, path=["response"])

    @parametrize
    def test_streaming_response_passthrough(self, client: Conductor) -> None:
        with client.end_users.with_streaming_response.passthrough(
            integration_slug="quickbooks_desktop",
            id="end_usr_1234567abcdefg",
            qbd_payload={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            end_user = response.parse()
            assert_matches_type(EndUserPassthroughResponse, end_user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_passthrough(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.end_users.with_raw_response.passthrough(
                integration_slug="quickbooks_desktop",
                id="",
                qbd_payload={"foo": "bar"},
            )

    @parametrize
    def test_method_ping(self, client: Conductor) -> None:
        end_user = client.end_users.ping(
            integration_slug="quickbooks_desktop",
            id="end_user_1234567abcdefg",
        )
        assert_matches_type(EndUserPingResponse, end_user, path=["response"])

    @parametrize
    def test_raw_response_ping(self, client: Conductor) -> None:
        response = client.end_users.with_raw_response.ping(
            integration_slug="quickbooks_desktop",
            id="end_user_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        end_user = response.parse()
        assert_matches_type(EndUserPingResponse, end_user, path=["response"])

    @parametrize
    def test_streaming_response_ping(self, client: Conductor) -> None:
        with client.end_users.with_streaming_response.ping(
            integration_slug="quickbooks_desktop",
            id="end_user_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            end_user = response.parse()
            assert_matches_type(EndUserPingResponse, end_user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_ping(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.end_users.with_raw_response.ping(
                integration_slug="quickbooks_desktop",
                id="",
            )


class TestAsyncEndUsers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncConductor) -> None:
        end_user = await async_client.end_users.create(
            company_name="Acme Inc.",
            email="alice@acme.com",
            source_id="12345678-abcd-abcd-example-1234567890ab",
        )
        assert_matches_type(EndUser, end_user, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncConductor) -> None:
        response = await async_client.end_users.with_raw_response.create(
            company_name="Acme Inc.",
            email="alice@acme.com",
            source_id="12345678-abcd-abcd-example-1234567890ab",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        end_user = await response.parse()
        assert_matches_type(EndUser, end_user, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncConductor) -> None:
        async with async_client.end_users.with_streaming_response.create(
            company_name="Acme Inc.",
            email="alice@acme.com",
            source_id="12345678-abcd-abcd-example-1234567890ab",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            end_user = await response.parse()
            assert_matches_type(EndUser, end_user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncConductor) -> None:
        end_user = await async_client.end_users.retrieve(
            "end_usr_1234567abcdefg",
        )
        assert_matches_type(EndUser, end_user, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncConductor) -> None:
        response = await async_client.end_users.with_raw_response.retrieve(
            "end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        end_user = await response.parse()
        assert_matches_type(EndUser, end_user, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncConductor) -> None:
        async with async_client.end_users.with_streaming_response.retrieve(
            "end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            end_user = await response.parse()
            assert_matches_type(EndUser, end_user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.end_users.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncConductor) -> None:
        end_user = await async_client.end_users.list()
        assert_matches_type(EndUserListResponse, end_user, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncConductor) -> None:
        response = await async_client.end_users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        end_user = await response.parse()
        assert_matches_type(EndUserListResponse, end_user, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncConductor) -> None:
        async with async_client.end_users.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            end_user = await response.parse()
            assert_matches_type(EndUserListResponse, end_user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncConductor) -> None:
        end_user = await async_client.end_users.delete(
            "end_usr_1234567abcdefg",
        )
        assert_matches_type(EndUserDeleteResponse, end_user, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncConductor) -> None:
        response = await async_client.end_users.with_raw_response.delete(
            "end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        end_user = await response.parse()
        assert_matches_type(EndUserDeleteResponse, end_user, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncConductor) -> None:
        async with async_client.end_users.with_streaming_response.delete(
            "end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            end_user = await response.parse()
            assert_matches_type(EndUserDeleteResponse, end_user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.end_users.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_passthrough(self, async_client: AsyncConductor) -> None:
        end_user = await async_client.end_users.passthrough(
            integration_slug="quickbooks_desktop",
            id="end_usr_1234567abcdefg",
            qbd_payload={"foo": "bar"},
        )
        assert_matches_type(EndUserPassthroughResponse, end_user, path=["response"])

    @parametrize
    async def test_raw_response_passthrough(self, async_client: AsyncConductor) -> None:
        response = await async_client.end_users.with_raw_response.passthrough(
            integration_slug="quickbooks_desktop",
            id="end_usr_1234567abcdefg",
            qbd_payload={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        end_user = await response.parse()
        assert_matches_type(EndUserPassthroughResponse, end_user, path=["response"])

    @parametrize
    async def test_streaming_response_passthrough(self, async_client: AsyncConductor) -> None:
        async with async_client.end_users.with_streaming_response.passthrough(
            integration_slug="quickbooks_desktop",
            id="end_usr_1234567abcdefg",
            qbd_payload={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            end_user = await response.parse()
            assert_matches_type(EndUserPassthroughResponse, end_user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_passthrough(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.end_users.with_raw_response.passthrough(
                integration_slug="quickbooks_desktop",
                id="",
                qbd_payload={"foo": "bar"},
            )

    @parametrize
    async def test_method_ping(self, async_client: AsyncConductor) -> None:
        end_user = await async_client.end_users.ping(
            integration_slug="quickbooks_desktop",
            id="end_user_1234567abcdefg",
        )
        assert_matches_type(EndUserPingResponse, end_user, path=["response"])

    @parametrize
    async def test_raw_response_ping(self, async_client: AsyncConductor) -> None:
        response = await async_client.end_users.with_raw_response.ping(
            integration_slug="quickbooks_desktop",
            id="end_user_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        end_user = await response.parse()
        assert_matches_type(EndUserPingResponse, end_user, path=["response"])

    @parametrize
    async def test_streaming_response_ping(self, async_client: AsyncConductor) -> None:
        async with async_client.end_users.with_streaming_response.ping(
            integration_slug="quickbooks_desktop",
            id="end_user_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            end_user = await response.parse()
            assert_matches_type(EndUserPingResponse, end_user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_ping(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.end_users.with_raw_response.ping(
                integration_slug="quickbooks_desktop",
                id="",
            )
