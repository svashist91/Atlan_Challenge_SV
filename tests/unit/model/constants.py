DEFAULT = "default"
CONNECTOR_TYPE = "snowflake"
TIME_STAMP = "1686532494"
CONNECTION_NAME = "MyConnection"
DATABASE_NAME = "MyDB"
SCHEMA_NAME = "MySchema"
TABLE_NAME = "MyTable"
VIEW_NAME = "MyView"
COLUMN_NAME = "MyColumn"
GLOSSARY_NAME = "MyGlossary"
GLOSSARY_TERM_NAME = "MyTerm"
GLOSSARY_CATEGORY_NAME = "MyCategory"
AWS_ARN = "arn:aws:s3:::dev-atlan-sources/sample-data/wwi/STOCK_ITEMS/"
BUCKET_NAME = "bucket_123"
S3_OBJECT_NAME = "object"
S3_OBJECT_PREFIX = "/some/folder/structure"
S3_CONNECTION_QUALIFIED_NAME = "default/s3/1686535364"
S3_OBJECT_QUALIFIED_NAME = f"{S3_CONNECTION_QUALIFIED_NAME}/{AWS_ARN}"
BUCKET_QUALIFIED_NAME = f"{S3_CONNECTION_QUALIFIED_NAME}/{AWS_ARN}"
BUCKET_WITH_NAME_QUALIFIED_NAME = f"{S3_CONNECTION_QUALIFIED_NAME}/{BUCKET_NAME}"
GLOSSARY_QUALIFIED_NAME = "OpU9a9kG825gAqpamXugf"
GLOSSARY_TERM_QUALIFIED_NAME = "0KVjsIaDcseinHYE7Nq0w@OpU9a9kG825gAqpamXugf"
GLOSSARY_CATEGORY_QUALIFIED_NAME = "1KsdsIaDcseinHYE7Nq0w@OpU9a9kG825gAqpamXugf"
CONNECTION_QUALIFIED_NAME = f"{DEFAULT}/{CONNECTOR_TYPE}/{TIME_STAMP}"
DATABASE_QUALIFIED_NAME = f"{CONNECTION_QUALIFIED_NAME}/{DATABASE_NAME}"
SCHEMA_QUALIFIED_NAME = f"{DATABASE_QUALIFIED_NAME}/{SCHEMA_NAME}"
TABLE_QUALIFIED_NAME = f"{SCHEMA_QUALIFIED_NAME}/{TABLE_NAME}"
VIEW_QUALIFIED_NAME = f"{SCHEMA_QUALIFIED_NAME}/{VIEW_NAME}"
TABLE_COLUMN_QUALIFIED_NAME = f"{TABLE_QUALIFIED_NAME}/{COLUMN_NAME}"
VIEW_COLUMN_QUALIFIED_NAME = f"{VIEW_QUALIFIED_NAME}/{COLUMN_NAME}"
FILE_NAME = "file.pdf"
FILE_CONNECTION_QUALIFIED_NAME = "default/api/1686535364"
FILE_QUALIFIED_NAME = f"{FILE_CONNECTION_QUALIFIED_NAME}/{FILE_NAME}"
ADLS_ACCOUNT_NAME = "myaccount"
ADLS_CONNECTION_QUALIFIED_NAME = "default/adls/1686535364"
ADLS_QUALIFIED_NAME = f"{ADLS_CONNECTION_QUALIFIED_NAME}/{ADLS_ACCOUNT_NAME}"  # "default/adls/123456789/myaccount"
ADLS_CONNECTOR_TYPE = "adls"
ADLS_CONTAINER_NAME = "mycontainer"
ADLS_OBJECT_NAME = "myobject.csv"
ADLS_ACCOUNT_QUALIFIED_NAME = (
    f"{ADLS_QUALIFIED_NAME}"  # "default/adls/123456789/myaccount"
)
# "default/adls/123456789/myaccount/mycontainer"
ADLS_CONTAINER_QUALIFIED_NAME = f"{ADLS_QUALIFIED_NAME}/{ADLS_CONTAINER_NAME}"
# "default/adls/123456789/myaccount/mycontainer/myobject.csv"
ADLS_OBJECT_QUALIFIED_NAME = f"{ADLS_CONTAINER_QUALIFIED_NAME}/{ADLS_OBJECT_NAME}"
API_SPEC_NAME = "api-spec"
API_PATH_NAME = "/api/path"
API_OBJECT_NAME = "api-object"
API_OBJECT_REF_NAME = "api-object-ref"
API_QUERY_NAME = "api-query"
API_FIELD_NAME = "api-field"
API_CONNECTION_QUALIFIED_NAME = "default/api/123456789"
API_QUALIFIED_NAME = f"{API_CONNECTION_QUALIFIED_NAME}/{API_SPEC_NAME}"
API_CONNECTOR_TYPE = "api"
API_PATH_RAW_URI = "/api/path"
API_SPEC_QUALIFIED_NAME = f"{API_CONNECTION_QUALIFIED_NAME}/{API_SPEC_NAME}"
API_PATH_QUALIFIED_NAME = (
    f"{API_CONNECTION_QUALIFIED_NAME}/{API_SPEC_NAME}{API_PATH_RAW_URI}"
)
API_OBJECT_QUALIFIED_NAME = f"{API_CONNECTION_QUALIFIED_NAME}/{API_OBJECT_NAME}"
API_QUERY_QUALIFIED_NAME = f"{API_CONNECTION_QUALIFIED_NAME}/{API_QUERY_NAME}"
API_QUERY_REFERENCE_OBJECT_QN = f"{API_CONNECTION_QUALIFIED_NAME}/{API_OBJECT_REF_NAME}"
API_FIELD_PARENT_OBJECT_QUALIFIED_NAME = (
    f"{API_CONNECTION_QUALIFIED_NAME}/{API_OBJECT_NAME}"
)
API_FIELD_PARENT_QUERY_QUALIFIED_NAME = (
    f"{API_CONNECTION_QUALIFIED_NAME}/{API_QUERY_NAME}"
)
API_FIELD_REFERENCE_OBJECT_QN = f"{API_CONNECTION_QUALIFIED_NAME}/{API_OBJECT_REF_NAME}"
GCS_BUCKET_NAME = "mybucket"
GCS_CONNECTION_QUALIFIED_NAME = "default/gcs/123456789"
GCS_QUALIFIED_NAME = f"{GCS_CONNECTION_QUALIFIED_NAME}/{GCS_BUCKET_NAME}"
GCS_CONNECTOR_TYPE = "gcs"
GCS_OBJECT_NAME = "myobject.csv"
GCS_BUCKET_QUALIFIED_NAME = f"{GCS_QUALIFIED_NAME}"
GCS_OBJECT_QUALIFIED_NAME = f"{GCS_QUALIFIED_NAME}/{GCS_OBJECT_NAME}"
REPORT_NAME = "gds-report"
SOURCE_NAME = "gds-source"
DATASTUDIO_CONNECTION_QUALIFIED_NAME = "default/datastudio/123456789"
QUALIFIED_NAME_REPORT = f"{DATASTUDIO_CONNECTION_QUALIFIED_NAME}/{REPORT_NAME}"
QUALIFIED_NAME_SOURCE = f"{DATASTUDIO_CONNECTION_QUALIFIED_NAME}/{SOURCE_NAME}"
CONNECTOR_NAME = "datastudio"
PRESET_WORKSPACE_NAME = "ps-workspace"
PRESET_CONNECTION_QUALIFIED_NAME = "default/preset/123456789"
PRESET_WORKSPACE_QUALIFIED_NAME = (
    f"{PRESET_CONNECTION_QUALIFIED_NAME}/{PRESET_WORKSPACE_NAME}"
)
PRESET_CONNECTOR_TYPE = "preset"
PRESET_DASHBOARD_NAME = "ps-collection"
PRESET_DASHBOARD_QUALIFIED_NAME = f"{PRESET_CONNECTION_QUALIFIED_NAME}/{PRESET_WORKSPACE_NAME}/{PRESET_DASHBOARD_NAME}"
PRESET_CHART_NAME = "ps-chart"
PRESET_CHART_QUALIFIED_NAME = f"{PRESET_DASHBOARD_QUALIFIED_NAME}/{PRESET_CHART_NAME}"
PRESET_DATASET_NAME = "ps-dataset"
PRESET_DATASET_QUALIFIED_NAME = (
    f"{PRESET_DASHBOARD_QUALIFIED_NAME}/{PRESET_DATASET_NAME}"
)
PERSONA_NAME = "my-persona"
PURPOSE_NAME = "my-purpose"
DATA_DOMAIN_NAME = "data-domain"
DATA_DOMAIN_QUALIFIED_NAME = f"default/domain/{DATA_DOMAIN_NAME}/super"
DATA_SUB_DOMAIN_NAME = "data-sub-domain"
DATA_SUB_DOMAIN_QUALIFIED_NAME = (
    f"{DATA_DOMAIN_QUALIFIED_NAME}/domain/{DATA_SUB_DOMAIN_NAME}"
)
DATA_PRODUCT_NAME = "data-product"
DATA_PRODUCT_QUALIFIED_NAME = (
    f"{DATA_DOMAIN_QUALIFIED_NAME}/product/{DATA_PRODUCT_NAME}"
)
DATA_PRODUCT_UNDER_SUB_DOMAIN_QUALIFIED_NAME = (
    f"{DATA_SUB_DOMAIN_QUALIFIED_NAME}/product/{DATA_PRODUCT_NAME}"
)
ASSET_QUALIFIED_NAME = "default/snowflake/1234567890/db/schema/test-table"
DATA_CONTRACT_NAME_DEFAULT = "Data contract for test-table"
DATA_CONTRACT_QUALIFIED_NAME = f"{ASSET_QUALIFIED_NAME}/contract"
DATA_CONTRACT_JSON = {
    "type": "Table",
    "status": "DRAFT",
    "kind": "DataContract",
    "data_source": "some-asset-connection-name",
    "dataset": "some-asset-name",
}
DATA_CONTRACT_SPEC_STR = """
kind: DataContract
status: draft
template_version: 0.0.2
type: Table
dataset: some-asset-name
description: ''
columns:
- name: OWNER_ID
  description: ''
  data_type: VARCHAR
- name: CREATED_BY_ID
  description: ''
  data_type: VARCHAR
"""
DATA_CONTRACT_SPEC_STR_WITHOUT_DATASET = """
kind: DataContract
status: draft
template_version: 0.0.2
type: Table
description: ''
columns:
- name: OWNER_ID
  description: ''
  data_type: VARCHAR
- name: CREATED_BY_ID
  description: ''
  data_type: VARCHAR
"""
DATA_CONTRACT_NAME = f"Data contract for {DATA_CONTRACT_JSON['dataset']}"
CP_NAME = "column-process"
CP_PROCESS_ID = "cp-process-id"
CP_CONNECTION_QUALIFIED_NAME = "default/vertica/123456789"
CP_QUALIFIED_NAME_HASH = (
    f"{CP_CONNECTION_QUALIFIED_NAME}/ecb5f77380c04710c979acfb8d3bba2f"
)
CP_QUALIFIED_NAME = f"{CP_CONNECTION_QUALIFIED_NAME}/{CP_PROCESS_ID}"
AIRFLOW_DAG_NAME = "test-airflow-dag"
AIRFLOW_CONNECTION_QUALIFIED_NAME = "default/airflow/123456789"
AIRFLOW_DAG_QUALIFIED_NAME = f"{AIRFLOW_CONNECTION_QUALIFIED_NAME}/{AIRFLOW_DAG_NAME}"
AIRFLOW_TASK_NAME = "test-airflow-task"
AIRFLOW_TASK_QUALIFIED_NAME = f"{AIRFLOW_DAG_QUALIFIED_NAME}/{AIRFLOW_TASK_NAME}"
KAFKA_TOPIC_NAME = "test-kafka-topic"
KAFKA_TOPIC_NAME_2 = f"{KAFKA_TOPIC_NAME}-2"
KAFKA_CONNECTION_QUALIFIED_NAME = "default/kafka/123456789"
KAFKA_TOPIC_QUALIFIED_NAME = (
    f"{KAFKA_CONNECTION_QUALIFIED_NAME}/topic/{KAFKA_TOPIC_NAME}"
)
KAFKA_TOPIC_QUALIFIED_NAMES = [
    KAFKA_TOPIC_QUALIFIED_NAME,
    f"{KAFKA_CONNECTION_QUALIFIED_NAME}/topic/{KAFKA_TOPIC_NAME_2}",
]
KAFKA_CONSUMER_GROUP_NAME = "test-kafka-cg"
KAFKA_CONSUMER_GROUP_QUALIFIED_NAME = (
    f"{KAFKA_CONNECTION_QUALIFIED_NAME}/consumer-group/{KAFKA_CONSUMER_GROUP_NAME}"
)
EVENT_HUB_NAME = "test-event-hub"
EVENT_HUB_NAME_2 = f"{EVENT_HUB_NAME}-2"
EVENT_HUB_CONNECTION_QUALIFIED_NAME = "default/azure-event-hub/123456789"
EVENT_HUB_QUALIFIED_NAME = (
    f"{EVENT_HUB_CONNECTION_QUALIFIED_NAME}/topic/{EVENT_HUB_NAME}"
)
EVENT_HUB_QUALIFIED_NAMES = [
    EVENT_HUB_QUALIFIED_NAME,
    f"{EVENT_HUB_CONNECTION_QUALIFIED_NAME}/topic/{EVENT_HUB_NAME_2}",
]
EVENT_HUB_CONSUMER_GROUP_NAME = "test-event-cg"
EVENT_HUB_CONSUMER_GROUP_QUALIFIED_NAME = (
    f"{EVENT_HUB_CONNECTION_QUALIFIED_NAME}/consumer-group"
    f"/{EVENT_HUB_NAME}/{EVENT_HUB_CONSUMER_GROUP_NAME}"
)
SUPERSET_CONNECTION_QUALIFIED_NAME = "default/superset/123456789"
SUPERSET_CONNECTOR_TYPE = "superset"
SUPERSET_DASHBOARD_NAME = "ss-dashboard"
SUPERSET_DASHBOARD_QUALIFIED_NAME = (
    f"{SUPERSET_CONNECTION_QUALIFIED_NAME}/{SUPERSET_DASHBOARD_NAME}"
)
SUPERSET_CHART_NAME = "ss-chart"
SUPERSET_CHART_QUALIFIED_NAME = (
    f"{SUPERSET_DASHBOARD_QUALIFIED_NAME}/{SUPERSET_CHART_NAME}"
)
SUPERSET_DATASET_NAME = "ss-dataset"
SUPERSET_DATASET_QUALIFIED_NAME = (
    f"{SUPERSET_DASHBOARD_QUALIFIED_NAME}/{SUPERSET_DATASET_NAME}"
)