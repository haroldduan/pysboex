<#
**** Programmer:Harold.Duan
**** Date:20200627
**** Reason: Unit test running scripts.
#>

pytest --html=./scripts/test_report/testrpt.html --self-contained-html
# pytest --html=./scripts/test_report/test_report.html
# pytest --cov-report=html --cov=./ ./scripts/test_report
pytest --cov=src tests --cov-report=html --cov-config=./scripts/.coveragerc
