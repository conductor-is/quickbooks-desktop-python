# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor._utils import parse_date
from conductor.types.qbd import (
    ReportJobResponse,
    ReportTimeResponse,
    ReportAgingResponse,
    ReportCustomDetailResponse,
    ReportBudgetSummaryResponse,
    ReportCustomSummaryResponse,
    ReportGeneralDetailResponse,
    ReportPayrollDetailResponse,
    ReportGeneralSummaryResponse,
    ReportPayrollSummaryResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReports:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_aging(self, client: Conductor) -> None:
        report = client.qbd.reports.aging(
            report_type="ap_aging_detail",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(ReportAgingResponse, report, path=["response"])

    @parametrize
    def test_method_aging_with_all_params(self, client: Conductor) -> None:
        report = client.qbd.reports.aging(
            report_type="ap_aging_detail",
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_full_names=["Corporate:Accounts-Payable"],
            account_ids=["80000001-1234567890"],
            accounts_to_include="all",
            account_type="bank",
            aging_as_of="report_end_date",
            class_full_names=["Department:Marketing"],
            class_ids=["80000001-1234567890"],
            detail_level="all_except_summary",
            entity_full_names=["ABC Corporation:Website Redesign Project"],
            entity_ids=["80000001-1234567890"],
            entity_type="customer",
            include_columns=["date", "transaction_type", "amount"],
            item_full_names=["Services:Consulting"],
            item_ids=["80000001-1234567890"],
            item_type="inventory",
            posting_status="posting",
            report_date_from=parse_date("2025-01-01"),
            report_date_macro="this_year_to_date",
            report_date_to=parse_date("2025-02-01"),
            transaction_types=["invoice", "sales_receipt"],
            updated_after=parse_date("2025-01-01"),
            updated_before=parse_date("2025-02-01"),
            updated_date_macro="this_month_to_date",
        )
        assert_matches_type(ReportAgingResponse, report, path=["response"])

    @parametrize
    def test_raw_response_aging(self, client: Conductor) -> None:
        response = client.qbd.reports.with_raw_response.aging(
            report_type="ap_aging_detail",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportAgingResponse, report, path=["response"])

    @parametrize
    def test_streaming_response_aging(self, client: Conductor) -> None:
        with client.qbd.reports.with_streaming_response.aging(
            report_type="ap_aging_detail",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportAgingResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_budget_summary(self, client: Conductor) -> None:
        report = client.qbd.reports.budget_summary(
            fiscal_year=2026,
            report_type="balance_sheet_budget_overview",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(ReportBudgetSummaryResponse, report, path=["response"])

    @parametrize
    def test_method_budget_summary_with_all_params(self, client: Conductor) -> None:
        report = client.qbd.reports.budget_summary(
            fiscal_year=2026,
            report_type="balance_sheet_budget_overview",
            conductor_end_user_id="end_usr_1234567abcdefg",
            budget_criterion="accounts",
            class_full_names=["Department:Marketing"],
            class_ids=["80000001-1234567890"],
            report_date_from=parse_date("2025-01-01"),
            report_date_macro="this_year_to_date",
            report_date_to=parse_date("2025-02-01"),
            summarize_columns_by="date",
            summarize_rows_by="account",
        )
        assert_matches_type(ReportBudgetSummaryResponse, report, path=["response"])

    @parametrize
    def test_raw_response_budget_summary(self, client: Conductor) -> None:
        response = client.qbd.reports.with_raw_response.budget_summary(
            fiscal_year=2026,
            report_type="balance_sheet_budget_overview",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportBudgetSummaryResponse, report, path=["response"])

    @parametrize
    def test_streaming_response_budget_summary(self, client: Conductor) -> None:
        with client.qbd.reports.with_streaming_response.budget_summary(
            fiscal_year=2026,
            report_type="balance_sheet_budget_overview",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportBudgetSummaryResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_custom_detail(self, client: Conductor) -> None:
        report = client.qbd.reports.custom_detail(
            include_columns=["date", "transaction_type", "amount"],
            summarize_rows_by="account",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(ReportCustomDetailResponse, report, path=["response"])

    @parametrize
    def test_method_custom_detail_with_all_params(self, client: Conductor) -> None:
        report = client.qbd.reports.custom_detail(
            include_columns=["date", "transaction_type", "amount"],
            summarize_rows_by="account",
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_full_names=["Corporate:Accounts-Payable"],
            account_ids=["80000001-1234567890"],
            accounts_to_include="all",
            account_type="bank",
            basis="accrual",
            class_full_names=["Department:Marketing"],
            class_ids=["80000001-1234567890"],
            detail_level="all_except_summary",
            entity_full_names=["ABC Corporation:Website Redesign Project"],
            entity_ids=["80000001-1234567890"],
            entity_type="customer",
            item_full_names=["Services:Consulting"],
            item_ids=["80000001-1234567890"],
            item_type="inventory",
            open_balance_as_of="report_end_date",
            posting_status="posting",
            report_date_from=parse_date("2025-01-01"),
            report_date_macro="this_year_to_date",
            report_date_to=parse_date("2025-02-01"),
            report_type="custom_transaction_detail",
            transaction_types=["invoice", "sales_receipt"],
            updated_after=parse_date("2025-01-01"),
            updated_before=parse_date("2025-02-01"),
            updated_date_macro="this_month_to_date",
        )
        assert_matches_type(ReportCustomDetailResponse, report, path=["response"])

    @parametrize
    def test_raw_response_custom_detail(self, client: Conductor) -> None:
        response = client.qbd.reports.with_raw_response.custom_detail(
            include_columns=["date", "transaction_type", "amount"],
            summarize_rows_by="account",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportCustomDetailResponse, report, path=["response"])

    @parametrize
    def test_streaming_response_custom_detail(self, client: Conductor) -> None:
        with client.qbd.reports.with_streaming_response.custom_detail(
            include_columns=["date", "transaction_type", "amount"],
            summarize_rows_by="account",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportCustomDetailResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_custom_summary(self, client: Conductor) -> None:
        report = client.qbd.reports.custom_summary(
            summarize_columns_by="month",
            summarize_rows_by="account",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(ReportCustomSummaryResponse, report, path=["response"])

    @parametrize
    def test_method_custom_summary_with_all_params(self, client: Conductor) -> None:
        report = client.qbd.reports.custom_summary(
            summarize_columns_by="month",
            summarize_rows_by="account",
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_full_names=["Corporate:Accounts-Payable"],
            account_ids=["80000001-1234567890"],
            account_type="bank",
            basis="accrual",
            class_full_names=["Department:Marketing"],
            class_ids=["80000001-1234567890"],
            columns_to_return="all",
            detail_level="all_except_summary",
            entity_full_names=["ABC Corporation:Website Redesign Project"],
            entity_ids=["80000001-1234567890"],
            entity_type="customer",
            include_subcolumns=True,
            item_full_names=["Services:Consulting"],
            item_ids=["80000001-1234567890"],
            item_type="inventory",
            posting_status="posting",
            report_calendar="calendar_year",
            report_date_from=parse_date("2025-01-01"),
            report_date_macro="this_year_to_date",
            report_date_to=parse_date("2025-02-01"),
            report_type="custom_summary",
            rows_to_return="all",
            transaction_types=["invoice", "sales_receipt"],
            updated_after=parse_date("2025-01-01"),
            updated_before=parse_date("2025-02-01"),
            updated_date_macro="this_month_to_date",
        )
        assert_matches_type(ReportCustomSummaryResponse, report, path=["response"])

    @parametrize
    def test_raw_response_custom_summary(self, client: Conductor) -> None:
        response = client.qbd.reports.with_raw_response.custom_summary(
            summarize_columns_by="month",
            summarize_rows_by="account",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportCustomSummaryResponse, report, path=["response"])

    @parametrize
    def test_streaming_response_custom_summary(self, client: Conductor) -> None:
        with client.qbd.reports.with_streaming_response.custom_summary(
            summarize_columns_by="month",
            summarize_rows_by="account",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportCustomSummaryResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_general_detail(self, client: Conductor) -> None:
        report = client.qbd.reports.general_detail(
            report_type="1099_detail",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(ReportGeneralDetailResponse, report, path=["response"])

    @parametrize
    def test_method_general_detail_with_all_params(self, client: Conductor) -> None:
        report = client.qbd.reports.general_detail(
            report_type="1099_detail",
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_full_names=["Corporate:Accounts-Payable"],
            account_ids=["80000001-1234567890"],
            accounts_to_include="all",
            account_type="bank",
            basis="accrual",
            class_full_names=["Department:Marketing"],
            class_ids=["80000001-1234567890"],
            detail_level="all_except_summary",
            entity_full_names=["ABC Corporation:Website Redesign Project"],
            entity_ids=["80000001-1234567890"],
            entity_type="customer",
            include_columns=["date", "transaction_type", "amount"],
            item_full_names=["Services:Consulting"],
            item_ids=["80000001-1234567890"],
            item_type="inventory",
            open_balance_as_of="report_end_date",
            posting_status="posting",
            report_date_from=parse_date("2025-01-01"),
            report_date_macro="this_year_to_date",
            report_date_to=parse_date("2025-02-01"),
            summarize_rows_by="account",
            transaction_types=["invoice", "sales_receipt"],
            updated_after=parse_date("2025-01-01"),
            updated_before=parse_date("2025-02-01"),
            updated_date_macro="this_month_to_date",
        )
        assert_matches_type(ReportGeneralDetailResponse, report, path=["response"])

    @parametrize
    def test_raw_response_general_detail(self, client: Conductor) -> None:
        response = client.qbd.reports.with_raw_response.general_detail(
            report_type="1099_detail",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportGeneralDetailResponse, report, path=["response"])

    @parametrize
    def test_streaming_response_general_detail(self, client: Conductor) -> None:
        with client.qbd.reports.with_streaming_response.general_detail(
            report_type="1099_detail",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportGeneralDetailResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_general_summary(self, client: Conductor) -> None:
        report = client.qbd.reports.general_summary(
            report_type="balance_sheet_by_class",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(ReportGeneralSummaryResponse, report, path=["response"])

    @parametrize
    def test_method_general_summary_with_all_params(self, client: Conductor) -> None:
        report = client.qbd.reports.general_summary(
            report_type="balance_sheet_by_class",
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_full_names=["Corporate:Accounts-Payable"],
            account_ids=["80000001-1234567890"],
            account_type="bank",
            basis="accrual",
            class_full_names=["Department:Marketing"],
            class_ids=["80000001-1234567890"],
            columns_to_return="all",
            detail_level="all_except_summary",
            entity_full_names=["ABC Corporation:Website Redesign Project"],
            entity_ids=["80000001-1234567890"],
            entity_type="customer",
            include_subcolumns=True,
            item_full_names=["Services:Consulting"],
            item_ids=["80000001-1234567890"],
            item_type="inventory",
            posting_status="posting",
            report_calendar="calendar_year",
            report_date_from=parse_date("2025-01-01"),
            report_date_macro="this_year_to_date",
            report_date_to=parse_date("2025-02-01"),
            rows_to_return="all",
            summarize_columns_by="month",
            transaction_types=["invoice", "sales_receipt"],
            updated_after=parse_date("2025-01-01"),
            updated_before=parse_date("2025-02-01"),
            updated_date_macro="this_month_to_date",
        )
        assert_matches_type(ReportGeneralSummaryResponse, report, path=["response"])

    @parametrize
    def test_raw_response_general_summary(self, client: Conductor) -> None:
        response = client.qbd.reports.with_raw_response.general_summary(
            report_type="balance_sheet_by_class",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportGeneralSummaryResponse, report, path=["response"])

    @parametrize
    def test_streaming_response_general_summary(self, client: Conductor) -> None:
        with client.qbd.reports.with_streaming_response.general_summary(
            report_type="balance_sheet_by_class",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportGeneralSummaryResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_job(self, client: Conductor) -> None:
        report = client.qbd.reports.job(
            report_type="item_estimates_vs_actuals",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(ReportJobResponse, report, path=["response"])

    @parametrize
    def test_method_job_with_all_params(self, client: Conductor) -> None:
        report = client.qbd.reports.job(
            report_type="item_estimates_vs_actuals",
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_full_names=["Corporate:Accounts-Payable"],
            account_ids=["80000001-1234567890"],
            account_type="bank",
            class_full_names=["Department:Marketing"],
            class_ids=["80000001-1234567890"],
            detail_level="all_except_summary",
            entity_full_names=["ABC Corporation:Website Redesign Project"],
            entity_ids=["80000001-1234567890"],
            entity_type="customer",
            include_subcolumns=True,
            item_full_names=["Services:Consulting"],
            item_ids=["80000001-1234567890"],
            item_type="inventory",
            posting_status="posting",
            report_date_from=parse_date("2025-01-01"),
            report_date_macro="this_year_to_date",
            report_date_to=parse_date("2025-02-01"),
            summarize_columns_by="month",
            transaction_types=["invoice", "sales_receipt"],
            updated_after=parse_date("2025-01-01"),
            updated_before=parse_date("2025-02-01"),
            updated_date_macro="this_month_to_date",
        )
        assert_matches_type(ReportJobResponse, report, path=["response"])

    @parametrize
    def test_raw_response_job(self, client: Conductor) -> None:
        response = client.qbd.reports.with_raw_response.job(
            report_type="item_estimates_vs_actuals",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportJobResponse, report, path=["response"])

    @parametrize
    def test_streaming_response_job(self, client: Conductor) -> None:
        with client.qbd.reports.with_streaming_response.job(
            report_type="item_estimates_vs_actuals",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportJobResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_payroll_detail(self, client: Conductor) -> None:
        report = client.qbd.reports.payroll_detail(
            report_type="employee_state_taxes_detail",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(ReportPayrollDetailResponse, report, path=["response"])

    @parametrize
    def test_method_payroll_detail_with_all_params(self, client: Conductor) -> None:
        report = client.qbd.reports.payroll_detail(
            report_type="employee_state_taxes_detail",
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_full_names=["Corporate:Accounts-Payable"],
            account_ids=["80000001-1234567890"],
            accounts_to_include="all",
            account_type="bank",
            class_full_names=["Department:Marketing"],
            class_ids=["80000001-1234567890"],
            detail_level="all_except_summary",
            entity_full_names=["ABC Corporation:Website Redesign Project"],
            entity_ids=["80000001-1234567890"],
            entity_type="customer",
            include_columns=["date", "transaction_type", "amount"],
            item_full_names=["Services:Consulting"],
            item_ids=["80000001-1234567890"],
            item_type="inventory",
            open_balance_as_of="report_end_date",
            posting_status="posting",
            report_date_from=parse_date("2025-01-01"),
            report_date_macro="this_year_to_date",
            report_date_to=parse_date("2025-02-01"),
            summarize_rows_by="account",
            updated_after=parse_date("2025-01-01"),
            updated_before=parse_date("2025-02-01"),
            updated_date_macro="this_month_to_date",
        )
        assert_matches_type(ReportPayrollDetailResponse, report, path=["response"])

    @parametrize
    def test_raw_response_payroll_detail(self, client: Conductor) -> None:
        response = client.qbd.reports.with_raw_response.payroll_detail(
            report_type="employee_state_taxes_detail",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportPayrollDetailResponse, report, path=["response"])

    @parametrize
    def test_streaming_response_payroll_detail(self, client: Conductor) -> None:
        with client.qbd.reports.with_streaming_response.payroll_detail(
            report_type="employee_state_taxes_detail",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportPayrollDetailResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_payroll_summary(self, client: Conductor) -> None:
        report = client.qbd.reports.payroll_summary(
            report_type="employee_earnings_summary",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(ReportPayrollSummaryResponse, report, path=["response"])

    @parametrize
    def test_method_payroll_summary_with_all_params(self, client: Conductor) -> None:
        report = client.qbd.reports.payroll_summary(
            report_type="employee_earnings_summary",
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_full_names=["Corporate:Accounts-Payable"],
            account_ids=["80000001-1234567890"],
            account_type="bank",
            class_full_names=["Department:Marketing"],
            class_ids=["80000001-1234567890"],
            columns_to_return="all",
            detail_level="all_except_summary",
            entity_full_names=["ABC Corporation:Website Redesign Project"],
            entity_ids=["80000001-1234567890"],
            entity_type="customer",
            include_subcolumns=True,
            item_full_names=["Services:Consulting"],
            item_ids=["80000001-1234567890"],
            item_type="inventory",
            posting_status="posting",
            report_calendar="calendar_year",
            report_date_from=parse_date("2025-01-01"),
            report_date_macro="this_year_to_date",
            report_date_to=parse_date("2025-02-01"),
            rows_to_return="all",
            summarize_columns_by="month",
            updated_after=parse_date("2025-01-01"),
            updated_before=parse_date("2025-02-01"),
            updated_date_macro="this_month_to_date",
        )
        assert_matches_type(ReportPayrollSummaryResponse, report, path=["response"])

    @parametrize
    def test_raw_response_payroll_summary(self, client: Conductor) -> None:
        response = client.qbd.reports.with_raw_response.payroll_summary(
            report_type="employee_earnings_summary",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportPayrollSummaryResponse, report, path=["response"])

    @parametrize
    def test_streaming_response_payroll_summary(self, client: Conductor) -> None:
        with client.qbd.reports.with_streaming_response.payroll_summary(
            report_type="employee_earnings_summary",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportPayrollSummaryResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_time(self, client: Conductor) -> None:
        report = client.qbd.reports.time(
            report_type="time_by_item",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(ReportTimeResponse, report, path=["response"])

    @parametrize
    def test_method_time_with_all_params(self, client: Conductor) -> None:
        report = client.qbd.reports.time(
            report_type="time_by_item",
            conductor_end_user_id="end_usr_1234567abcdefg",
            class_full_names=["Department:Marketing"],
            class_ids=["80000001-1234567890"],
            columns_to_return="all",
            entity_full_names=["ABC Corporation:Website Redesign Project"],
            entity_ids=["80000001-1234567890"],
            entity_type="customer",
            include_subcolumns=True,
            item_full_names=["Services:Consulting"],
            item_ids=["80000001-1234567890"],
            item_type="inventory",
            report_calendar="calendar_year",
            report_date_from=parse_date("2025-01-01"),
            report_date_macro="this_year_to_date",
            report_date_to=parse_date("2025-02-01"),
            rows_to_return="all",
            summarize_columns_by="month",
        )
        assert_matches_type(ReportTimeResponse, report, path=["response"])

    @parametrize
    def test_raw_response_time(self, client: Conductor) -> None:
        response = client.qbd.reports.with_raw_response.time(
            report_type="time_by_item",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportTimeResponse, report, path=["response"])

    @parametrize
    def test_streaming_response_time(self, client: Conductor) -> None:
        with client.qbd.reports.with_streaming_response.time(
            report_type="time_by_item",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportTimeResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncReports:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_aging(self, async_client: AsyncConductor) -> None:
        report = await async_client.qbd.reports.aging(
            report_type="ap_aging_detail",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(ReportAgingResponse, report, path=["response"])

    @parametrize
    async def test_method_aging_with_all_params(self, async_client: AsyncConductor) -> None:
        report = await async_client.qbd.reports.aging(
            report_type="ap_aging_detail",
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_full_names=["Corporate:Accounts-Payable"],
            account_ids=["80000001-1234567890"],
            accounts_to_include="all",
            account_type="bank",
            aging_as_of="report_end_date",
            class_full_names=["Department:Marketing"],
            class_ids=["80000001-1234567890"],
            detail_level="all_except_summary",
            entity_full_names=["ABC Corporation:Website Redesign Project"],
            entity_ids=["80000001-1234567890"],
            entity_type="customer",
            include_columns=["date", "transaction_type", "amount"],
            item_full_names=["Services:Consulting"],
            item_ids=["80000001-1234567890"],
            item_type="inventory",
            posting_status="posting",
            report_date_from=parse_date("2025-01-01"),
            report_date_macro="this_year_to_date",
            report_date_to=parse_date("2025-02-01"),
            transaction_types=["invoice", "sales_receipt"],
            updated_after=parse_date("2025-01-01"),
            updated_before=parse_date("2025-02-01"),
            updated_date_macro="this_month_to_date",
        )
        assert_matches_type(ReportAgingResponse, report, path=["response"])

    @parametrize
    async def test_raw_response_aging(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.reports.with_raw_response.aging(
            report_type="ap_aging_detail",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportAgingResponse, report, path=["response"])

    @parametrize
    async def test_streaming_response_aging(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.reports.with_streaming_response.aging(
            report_type="ap_aging_detail",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportAgingResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_budget_summary(self, async_client: AsyncConductor) -> None:
        report = await async_client.qbd.reports.budget_summary(
            fiscal_year=2026,
            report_type="balance_sheet_budget_overview",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(ReportBudgetSummaryResponse, report, path=["response"])

    @parametrize
    async def test_method_budget_summary_with_all_params(self, async_client: AsyncConductor) -> None:
        report = await async_client.qbd.reports.budget_summary(
            fiscal_year=2026,
            report_type="balance_sheet_budget_overview",
            conductor_end_user_id="end_usr_1234567abcdefg",
            budget_criterion="accounts",
            class_full_names=["Department:Marketing"],
            class_ids=["80000001-1234567890"],
            report_date_from=parse_date("2025-01-01"),
            report_date_macro="this_year_to_date",
            report_date_to=parse_date("2025-02-01"),
            summarize_columns_by="date",
            summarize_rows_by="account",
        )
        assert_matches_type(ReportBudgetSummaryResponse, report, path=["response"])

    @parametrize
    async def test_raw_response_budget_summary(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.reports.with_raw_response.budget_summary(
            fiscal_year=2026,
            report_type="balance_sheet_budget_overview",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportBudgetSummaryResponse, report, path=["response"])

    @parametrize
    async def test_streaming_response_budget_summary(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.reports.with_streaming_response.budget_summary(
            fiscal_year=2026,
            report_type="balance_sheet_budget_overview",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportBudgetSummaryResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_custom_detail(self, async_client: AsyncConductor) -> None:
        report = await async_client.qbd.reports.custom_detail(
            include_columns=["date", "transaction_type", "amount"],
            summarize_rows_by="account",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(ReportCustomDetailResponse, report, path=["response"])

    @parametrize
    async def test_method_custom_detail_with_all_params(self, async_client: AsyncConductor) -> None:
        report = await async_client.qbd.reports.custom_detail(
            include_columns=["date", "transaction_type", "amount"],
            summarize_rows_by="account",
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_full_names=["Corporate:Accounts-Payable"],
            account_ids=["80000001-1234567890"],
            accounts_to_include="all",
            account_type="bank",
            basis="accrual",
            class_full_names=["Department:Marketing"],
            class_ids=["80000001-1234567890"],
            detail_level="all_except_summary",
            entity_full_names=["ABC Corporation:Website Redesign Project"],
            entity_ids=["80000001-1234567890"],
            entity_type="customer",
            item_full_names=["Services:Consulting"],
            item_ids=["80000001-1234567890"],
            item_type="inventory",
            open_balance_as_of="report_end_date",
            posting_status="posting",
            report_date_from=parse_date("2025-01-01"),
            report_date_macro="this_year_to_date",
            report_date_to=parse_date("2025-02-01"),
            report_type="custom_transaction_detail",
            transaction_types=["invoice", "sales_receipt"],
            updated_after=parse_date("2025-01-01"),
            updated_before=parse_date("2025-02-01"),
            updated_date_macro="this_month_to_date",
        )
        assert_matches_type(ReportCustomDetailResponse, report, path=["response"])

    @parametrize
    async def test_raw_response_custom_detail(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.reports.with_raw_response.custom_detail(
            include_columns=["date", "transaction_type", "amount"],
            summarize_rows_by="account",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportCustomDetailResponse, report, path=["response"])

    @parametrize
    async def test_streaming_response_custom_detail(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.reports.with_streaming_response.custom_detail(
            include_columns=["date", "transaction_type", "amount"],
            summarize_rows_by="account",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportCustomDetailResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_custom_summary(self, async_client: AsyncConductor) -> None:
        report = await async_client.qbd.reports.custom_summary(
            summarize_columns_by="month",
            summarize_rows_by="account",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(ReportCustomSummaryResponse, report, path=["response"])

    @parametrize
    async def test_method_custom_summary_with_all_params(self, async_client: AsyncConductor) -> None:
        report = await async_client.qbd.reports.custom_summary(
            summarize_columns_by="month",
            summarize_rows_by="account",
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_full_names=["Corporate:Accounts-Payable"],
            account_ids=["80000001-1234567890"],
            account_type="bank",
            basis="accrual",
            class_full_names=["Department:Marketing"],
            class_ids=["80000001-1234567890"],
            columns_to_return="all",
            detail_level="all_except_summary",
            entity_full_names=["ABC Corporation:Website Redesign Project"],
            entity_ids=["80000001-1234567890"],
            entity_type="customer",
            include_subcolumns=True,
            item_full_names=["Services:Consulting"],
            item_ids=["80000001-1234567890"],
            item_type="inventory",
            posting_status="posting",
            report_calendar="calendar_year",
            report_date_from=parse_date("2025-01-01"),
            report_date_macro="this_year_to_date",
            report_date_to=parse_date("2025-02-01"),
            report_type="custom_summary",
            rows_to_return="all",
            transaction_types=["invoice", "sales_receipt"],
            updated_after=parse_date("2025-01-01"),
            updated_before=parse_date("2025-02-01"),
            updated_date_macro="this_month_to_date",
        )
        assert_matches_type(ReportCustomSummaryResponse, report, path=["response"])

    @parametrize
    async def test_raw_response_custom_summary(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.reports.with_raw_response.custom_summary(
            summarize_columns_by="month",
            summarize_rows_by="account",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportCustomSummaryResponse, report, path=["response"])

    @parametrize
    async def test_streaming_response_custom_summary(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.reports.with_streaming_response.custom_summary(
            summarize_columns_by="month",
            summarize_rows_by="account",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportCustomSummaryResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_general_detail(self, async_client: AsyncConductor) -> None:
        report = await async_client.qbd.reports.general_detail(
            report_type="1099_detail",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(ReportGeneralDetailResponse, report, path=["response"])

    @parametrize
    async def test_method_general_detail_with_all_params(self, async_client: AsyncConductor) -> None:
        report = await async_client.qbd.reports.general_detail(
            report_type="1099_detail",
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_full_names=["Corporate:Accounts-Payable"],
            account_ids=["80000001-1234567890"],
            accounts_to_include="all",
            account_type="bank",
            basis="accrual",
            class_full_names=["Department:Marketing"],
            class_ids=["80000001-1234567890"],
            detail_level="all_except_summary",
            entity_full_names=["ABC Corporation:Website Redesign Project"],
            entity_ids=["80000001-1234567890"],
            entity_type="customer",
            include_columns=["date", "transaction_type", "amount"],
            item_full_names=["Services:Consulting"],
            item_ids=["80000001-1234567890"],
            item_type="inventory",
            open_balance_as_of="report_end_date",
            posting_status="posting",
            report_date_from=parse_date("2025-01-01"),
            report_date_macro="this_year_to_date",
            report_date_to=parse_date("2025-02-01"),
            summarize_rows_by="account",
            transaction_types=["invoice", "sales_receipt"],
            updated_after=parse_date("2025-01-01"),
            updated_before=parse_date("2025-02-01"),
            updated_date_macro="this_month_to_date",
        )
        assert_matches_type(ReportGeneralDetailResponse, report, path=["response"])

    @parametrize
    async def test_raw_response_general_detail(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.reports.with_raw_response.general_detail(
            report_type="1099_detail",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportGeneralDetailResponse, report, path=["response"])

    @parametrize
    async def test_streaming_response_general_detail(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.reports.with_streaming_response.general_detail(
            report_type="1099_detail",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportGeneralDetailResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_general_summary(self, async_client: AsyncConductor) -> None:
        report = await async_client.qbd.reports.general_summary(
            report_type="balance_sheet_by_class",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(ReportGeneralSummaryResponse, report, path=["response"])

    @parametrize
    async def test_method_general_summary_with_all_params(self, async_client: AsyncConductor) -> None:
        report = await async_client.qbd.reports.general_summary(
            report_type="balance_sheet_by_class",
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_full_names=["Corporate:Accounts-Payable"],
            account_ids=["80000001-1234567890"],
            account_type="bank",
            basis="accrual",
            class_full_names=["Department:Marketing"],
            class_ids=["80000001-1234567890"],
            columns_to_return="all",
            detail_level="all_except_summary",
            entity_full_names=["ABC Corporation:Website Redesign Project"],
            entity_ids=["80000001-1234567890"],
            entity_type="customer",
            include_subcolumns=True,
            item_full_names=["Services:Consulting"],
            item_ids=["80000001-1234567890"],
            item_type="inventory",
            posting_status="posting",
            report_calendar="calendar_year",
            report_date_from=parse_date("2025-01-01"),
            report_date_macro="this_year_to_date",
            report_date_to=parse_date("2025-02-01"),
            rows_to_return="all",
            summarize_columns_by="month",
            transaction_types=["invoice", "sales_receipt"],
            updated_after=parse_date("2025-01-01"),
            updated_before=parse_date("2025-02-01"),
            updated_date_macro="this_month_to_date",
        )
        assert_matches_type(ReportGeneralSummaryResponse, report, path=["response"])

    @parametrize
    async def test_raw_response_general_summary(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.reports.with_raw_response.general_summary(
            report_type="balance_sheet_by_class",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportGeneralSummaryResponse, report, path=["response"])

    @parametrize
    async def test_streaming_response_general_summary(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.reports.with_streaming_response.general_summary(
            report_type="balance_sheet_by_class",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportGeneralSummaryResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_job(self, async_client: AsyncConductor) -> None:
        report = await async_client.qbd.reports.job(
            report_type="item_estimates_vs_actuals",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(ReportJobResponse, report, path=["response"])

    @parametrize
    async def test_method_job_with_all_params(self, async_client: AsyncConductor) -> None:
        report = await async_client.qbd.reports.job(
            report_type="item_estimates_vs_actuals",
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_full_names=["Corporate:Accounts-Payable"],
            account_ids=["80000001-1234567890"],
            account_type="bank",
            class_full_names=["Department:Marketing"],
            class_ids=["80000001-1234567890"],
            detail_level="all_except_summary",
            entity_full_names=["ABC Corporation:Website Redesign Project"],
            entity_ids=["80000001-1234567890"],
            entity_type="customer",
            include_subcolumns=True,
            item_full_names=["Services:Consulting"],
            item_ids=["80000001-1234567890"],
            item_type="inventory",
            posting_status="posting",
            report_date_from=parse_date("2025-01-01"),
            report_date_macro="this_year_to_date",
            report_date_to=parse_date("2025-02-01"),
            summarize_columns_by="month",
            transaction_types=["invoice", "sales_receipt"],
            updated_after=parse_date("2025-01-01"),
            updated_before=parse_date("2025-02-01"),
            updated_date_macro="this_month_to_date",
        )
        assert_matches_type(ReportJobResponse, report, path=["response"])

    @parametrize
    async def test_raw_response_job(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.reports.with_raw_response.job(
            report_type="item_estimates_vs_actuals",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportJobResponse, report, path=["response"])

    @parametrize
    async def test_streaming_response_job(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.reports.with_streaming_response.job(
            report_type="item_estimates_vs_actuals",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportJobResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_payroll_detail(self, async_client: AsyncConductor) -> None:
        report = await async_client.qbd.reports.payroll_detail(
            report_type="employee_state_taxes_detail",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(ReportPayrollDetailResponse, report, path=["response"])

    @parametrize
    async def test_method_payroll_detail_with_all_params(self, async_client: AsyncConductor) -> None:
        report = await async_client.qbd.reports.payroll_detail(
            report_type="employee_state_taxes_detail",
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_full_names=["Corporate:Accounts-Payable"],
            account_ids=["80000001-1234567890"],
            accounts_to_include="all",
            account_type="bank",
            class_full_names=["Department:Marketing"],
            class_ids=["80000001-1234567890"],
            detail_level="all_except_summary",
            entity_full_names=["ABC Corporation:Website Redesign Project"],
            entity_ids=["80000001-1234567890"],
            entity_type="customer",
            include_columns=["date", "transaction_type", "amount"],
            item_full_names=["Services:Consulting"],
            item_ids=["80000001-1234567890"],
            item_type="inventory",
            open_balance_as_of="report_end_date",
            posting_status="posting",
            report_date_from=parse_date("2025-01-01"),
            report_date_macro="this_year_to_date",
            report_date_to=parse_date("2025-02-01"),
            summarize_rows_by="account",
            updated_after=parse_date("2025-01-01"),
            updated_before=parse_date("2025-02-01"),
            updated_date_macro="this_month_to_date",
        )
        assert_matches_type(ReportPayrollDetailResponse, report, path=["response"])

    @parametrize
    async def test_raw_response_payroll_detail(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.reports.with_raw_response.payroll_detail(
            report_type="employee_state_taxes_detail",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportPayrollDetailResponse, report, path=["response"])

    @parametrize
    async def test_streaming_response_payroll_detail(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.reports.with_streaming_response.payroll_detail(
            report_type="employee_state_taxes_detail",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportPayrollDetailResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_payroll_summary(self, async_client: AsyncConductor) -> None:
        report = await async_client.qbd.reports.payroll_summary(
            report_type="employee_earnings_summary",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(ReportPayrollSummaryResponse, report, path=["response"])

    @parametrize
    async def test_method_payroll_summary_with_all_params(self, async_client: AsyncConductor) -> None:
        report = await async_client.qbd.reports.payroll_summary(
            report_type="employee_earnings_summary",
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_full_names=["Corporate:Accounts-Payable"],
            account_ids=["80000001-1234567890"],
            account_type="bank",
            class_full_names=["Department:Marketing"],
            class_ids=["80000001-1234567890"],
            columns_to_return="all",
            detail_level="all_except_summary",
            entity_full_names=["ABC Corporation:Website Redesign Project"],
            entity_ids=["80000001-1234567890"],
            entity_type="customer",
            include_subcolumns=True,
            item_full_names=["Services:Consulting"],
            item_ids=["80000001-1234567890"],
            item_type="inventory",
            posting_status="posting",
            report_calendar="calendar_year",
            report_date_from=parse_date("2025-01-01"),
            report_date_macro="this_year_to_date",
            report_date_to=parse_date("2025-02-01"),
            rows_to_return="all",
            summarize_columns_by="month",
            updated_after=parse_date("2025-01-01"),
            updated_before=parse_date("2025-02-01"),
            updated_date_macro="this_month_to_date",
        )
        assert_matches_type(ReportPayrollSummaryResponse, report, path=["response"])

    @parametrize
    async def test_raw_response_payroll_summary(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.reports.with_raw_response.payroll_summary(
            report_type="employee_earnings_summary",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportPayrollSummaryResponse, report, path=["response"])

    @parametrize
    async def test_streaming_response_payroll_summary(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.reports.with_streaming_response.payroll_summary(
            report_type="employee_earnings_summary",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportPayrollSummaryResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_time(self, async_client: AsyncConductor) -> None:
        report = await async_client.qbd.reports.time(
            report_type="time_by_item",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(ReportTimeResponse, report, path=["response"])

    @parametrize
    async def test_method_time_with_all_params(self, async_client: AsyncConductor) -> None:
        report = await async_client.qbd.reports.time(
            report_type="time_by_item",
            conductor_end_user_id="end_usr_1234567abcdefg",
            class_full_names=["Department:Marketing"],
            class_ids=["80000001-1234567890"],
            columns_to_return="all",
            entity_full_names=["ABC Corporation:Website Redesign Project"],
            entity_ids=["80000001-1234567890"],
            entity_type="customer",
            include_subcolumns=True,
            item_full_names=["Services:Consulting"],
            item_ids=["80000001-1234567890"],
            item_type="inventory",
            report_calendar="calendar_year",
            report_date_from=parse_date("2025-01-01"),
            report_date_macro="this_year_to_date",
            report_date_to=parse_date("2025-02-01"),
            rows_to_return="all",
            summarize_columns_by="month",
        )
        assert_matches_type(ReportTimeResponse, report, path=["response"])

    @parametrize
    async def test_raw_response_time(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.reports.with_raw_response.time(
            report_type="time_by_item",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportTimeResponse, report, path=["response"])

    @parametrize
    async def test_streaming_response_time(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.reports.with_streaming_response.time(
            report_type="time_by_item",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportTimeResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True
