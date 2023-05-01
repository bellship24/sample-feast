# Importing dependencies
from google.protobuf.duration_pb2 import Duration
from feast import Entity, Feature, FeatureView, FileSource, ValueType


# Declaring an entity gor the dataset
patient = Entity(
    name="patient_id",
    value_type=ValueType.INT64,
    description='The ID of the patient',
)

# Declaring the source of the first set of features
f_source1 = FileSource(
    path="data/data_df1.parquet",
    event_timestamp_column="event_timestamp",
)

# Defining the first set of features
df1_fv = FeatureView(
    name="df1_feature_view",
    ttl=Duration(seconds=84600 * 3),
    entities=["patient_id"],
    features=[
        Feature(name="mean radius", dtype=ValueType.FLOAT),
        Feature(name="mean texture", dtype=ValueType.FLOAT),
        Feature(name="mean perimeter", dtype=ValueType.FLOAT),
        Feature(name="mean area", dtype=ValueType.FLOAT),
        Feature(name="mean smoothness", dtype=ValueType.FLOAT),
    ],
    batch_source=f_source1,
)

