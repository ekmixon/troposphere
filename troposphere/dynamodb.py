# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSHelperFn, AWSObject, AWSProperty, If, Tags
from .validators import boolean, double, integer


def attribute_type_validator(x):
    valid_types = ["S", "N", "B"]
    if x not in valid_types:
        raise ValueError(f'AttributeType must be one of: {", ".join(valid_types)}')
    return x


def key_type_validator(x):
    valid_types = ["HASH", "RANGE"]
    if x not in valid_types:
        raise ValueError(f'KeyType must be one of: {", ".join(valid_types)}')
    return x


def projection_type_validator(x):
    valid_types = ["KEYS_ONLY", "INCLUDE", "ALL"]
    if x not in valid_types:
        raise ValueError(f'ProjectionType must be one of: {", ".join(valid_types)}')
    return x


def billing_mode_validator(x):
    valid_modes = ["PROVISIONED", "PAY_PER_REQUEST"]
    if x not in valid_modes:
        raise ValueError(
            f'Table billing mode must be one of: {", ".join(valid_modes)}'
        )

    return x


class AttributeDefinition(AWSProperty):
    props = {
        "AttributeName": (str, True),
        "AttributeType": (attribute_type_validator, True),
    }


class ContributorInsightsSpecification(AWSProperty):
    props = {
        "Enabled": (boolean, True),
    }


class KeySchema(AWSProperty):
    props = {"AttributeName": (str, True), "KeyType": (key_type_validator, True)}


class Key(KeySchema):
    """For backwards compatibility."""

    pass


class KinesisStreamSpecification(AWSProperty):
    props = {"StreamArn": (str, True)}


class ProvisionedThroughput(AWSProperty):
    props = {
        "ReadCapacityUnits": (int, True),
        "WriteCapacityUnits": (int, True),
    }


class Projection(AWSProperty):
    props = {
        "NonKeyAttributes": ([str], False),
        "ProjectionType": (projection_type_validator, False),
    }


class SSESpecification(AWSProperty):
    props = {
        "KMSMasterKeyId": (str, False),
        "SSEEnabled": (boolean, True),
        "SSEType": (str, False),
    }


class GlobalSecondaryIndex(AWSProperty):
    props = {
        "IndexName": (str, True),
        "KeySchema": ([KeySchema], True),
        "Projection": (Projection, True),
        "ProvisionedThroughput": (ProvisionedThroughput, False),
    }


class LocalSecondaryIndex(AWSProperty):
    props = {
        "IndexName": (str, True),
        "KeySchema": ([KeySchema], True),
        "Projection": (Projection, True),
    }


class PointInTimeRecoverySpecification(AWSProperty):
    props = {
        "PointInTimeRecoveryEnabled": (boolean, False),
    }


class StreamSpecification(AWSProperty):
    props = {
        "StreamViewType": (str, True),
    }


class TimeToLiveSpecification(AWSProperty):
    props = {
        "AttributeName": (str, True),
        "Enabled": (boolean, True),
    }


class TargetTrackingScalingPolicyConfiguration(AWSProperty):
    props = {
        "DisableScaleIn": (boolean, False),
        "ScaleInCooldown": (integer, False),
        "ScaleOutCooldown": (integer, False),
        "TargetValue": (double, True),
    }


class CapacityAutoScalingSettings(AWSProperty):
    props = {
        "MaxCapacity": (integer, True),
        "MinCapacity": (integer, True),
        "SeedCapacity": (integer, False),
        "TargetTrackingScalingPolicyConfiguration": (
            TargetTrackingScalingPolicyConfiguration,
            True,
        ),
    }


class TargetTrackingScalingPolicyConfiguration(AWSProperty):
    props = {
        "DisableScaleIn": (boolean, False),
        "ScaleInCooldown": (integer, False),
        "ScaleOutCooldown": (integer, False),
        "TargetValue": (double, True),
    }


class ReadProvisionedThroughputSettings(AWSProperty):
    props = {
        "ReadCapacityAutoScalingSettings": (CapacityAutoScalingSettings, False),
        "ReadCapacityUnits": (integer, False),
    }


class ReplicaGlobalSecondaryIndexSpecification(AWSProperty):
    props = {
        "ContributorInsightsSpecification": (ContributorInsightsSpecification, False),
        "IndexName": (str, True),
        "ReadProvisionedThroughputSettings": (ReadProvisionedThroughputSettings, False),
    }


class ReplicaSSESpecification(AWSProperty):
    props = {
        "KMSMasterKeyId": (str, True),
    }


class ReplicaSpecification(AWSProperty):
    props = {
        "ContributorInsightsSpecification": (ContributorInsightsSpecification, False),
        "GlobalSecondaryIndexes": ([ReplicaGlobalSecondaryIndexSpecification], False),
        "PointInTimeRecoverySpecification": (PointInTimeRecoverySpecification, False),
        "ReadProvisionedThroughputSettings": (ReadProvisionedThroughputSettings, False),
        "Region": (str, True),
        "SSESpecification": (ReplicaSSESpecification, False),
        "Tags": (Tags, False),
    }


class WriteProvisionedThroughputSettings(AWSProperty):
    props = {
        "WriteCapacityAutoScalingSettings": (CapacityAutoScalingSettings, False),
    }


class GlobalTable(AWSObject):
    resource_type = "AWS::DynamoDB::GlobalTable"

    props = {
        "AttributeDefinitions": ([AttributeDefinition], True),
        "BillingMode": (str, False),
        "GlobalSecondaryIndexes": ([GlobalSecondaryIndex], False),
        "KeySchema": ([KeySchema], True),
        "LocalSecondaryIndexes": ([LocalSecondaryIndex], False),
        "Replicas": ([ReplicaSpecification], True),
        "SSESpecification": (SSESpecification, False),
        "StreamSpecification": (StreamSpecification, False),
        "TableName": (str, False),
        "TimeToLiveSpecification": (TimeToLiveSpecification, False),
        "WriteProvisionedThroughputSettings": (
            WriteProvisionedThroughputSettings,
            False,
        ),
    }


class Table(AWSObject):
    resource_type = "AWS::DynamoDB::Table"

    props = {
        "AttributeDefinitions": ([AttributeDefinition], True),
        "BillingMode": (billing_mode_validator, False),
        "ContributorInsightsSpecification": (ContributorInsightsSpecification, False),
        "GlobalSecondaryIndexes": ([GlobalSecondaryIndex], False),
        "KeySchema": ([KeySchema], True),
        "KinesisStreamSpecification": (KinesisStreamSpecification, False),
        "LocalSecondaryIndexes": ([LocalSecondaryIndex], False),
        "PointInTimeRecoverySpecification": (PointInTimeRecoverySpecification, False),
        "ProvisionedThroughput": (ProvisionedThroughput, False),
        "SSESpecification": (SSESpecification, False),
        "StreamSpecification": (StreamSpecification, False),
        "TableName": (str, False),
        "Tags": (Tags, False),
        "TimeToLiveSpecification": (TimeToLiveSpecification, False),
    }

    def validate(self):
        billing_mode = self.properties.get("BillingMode", "PROVISIONED")
        indexes = self.properties.get("GlobalSecondaryIndexes", [])
        tput_props = [self.properties]
        tput_props.extend(
            [x.properties for x in indexes if not isinstance(x, AWSHelperFn)]
        )

        def check_if_all(name, props):
            validated = []
            for prop in props:
                is_helper = isinstance(prop.get(name), AWSHelperFn)
                validated.append(name in prop or is_helper)
            return all(validated)

        def check_any(name, props):
            validated = []
            for prop in props:
                is_helper = isinstance(prop.get(name), AWSHelperFn)
                validated.append(name in prop and not is_helper)
            return any(validated)

        if isinstance(billing_mode, If):
            if check_any("ProvisionedThroughput", tput_props):
                raise ValueError(
                    "Table billing mode is per-request. "
                    "ProvisionedThroughput property is mutually exclusive"
                )
            return

        if billing_mode == "PROVISIONED":
            if not check_if_all("ProvisionedThroughput", tput_props):
                raise ValueError(
                    "Table billing mode is provisioned. "
                    "ProvisionedThroughput required if available"
                )
        elif billing_mode == "PAY_PER_REQUEST":
            if check_any("ProvisionedThroughput", tput_props):
                raise ValueError(
                    "Table billing mode is per-request. "
                    "ProvisionedThroughput property is mutually exclusive"
                )
