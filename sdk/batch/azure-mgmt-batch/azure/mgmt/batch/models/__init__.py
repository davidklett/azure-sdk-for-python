# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import ActivateApplicationPackageParameters
    from ._models_py3 import Application
    from ._models_py3 import ApplicationPackage
    from ._models_py3 import ApplicationPackageReference
    from ._models_py3 import AutoScaleRun
    from ._models_py3 import AutoScaleRunError
    from ._models_py3 import AutoScaleSettings
    from ._models_py3 import AutoStorageBaseProperties
    from ._models_py3 import AutoStorageProperties
    from ._models_py3 import AutoUserSpecification
    from ._models_py3 import AzureBlobFileSystemConfiguration
    from ._models_py3 import AzureFileShareConfiguration
    from ._models_py3 import BatchAccount
    from ._models_py3 import BatchAccountCreateParameters
    from ._models_py3 import BatchAccountKeys
    from ._models_py3 import BatchAccountRegenerateKeyParameters
    from ._models_py3 import BatchAccountUpdateParameters
    from ._models_py3 import BatchLocationQuota
    from ._models_py3 import Certificate
    from ._models_py3 import CertificateBaseProperties
    from ._models_py3 import CertificateCreateOrUpdateParameters
    from ._models_py3 import CertificateReference
    from ._models_py3 import CheckNameAvailabilityParameters
    from ._models_py3 import CheckNameAvailabilityResult
    from ._models_py3 import CIFSMountConfiguration
    from ._models_py3 import CloudServiceConfiguration
    from ._models_py3 import ContainerConfiguration
    from ._models_py3 import ContainerRegistry
    from ._models_py3 import DataDisk
    from ._models_py3 import DeleteCertificateError
    from ._models_py3 import DeploymentConfiguration
    from ._models_py3 import EnvironmentSetting
    from ._models_py3 import FixedScaleSettings
    from ._models_py3 import ImageReference
    from ._models_py3 import InboundNatPool
    from ._models_py3 import KeyVaultReference
    from ._models_py3 import LinuxUserConfiguration
    from ._models_py3 import MetadataItem
    from ._models_py3 import MountConfiguration
    from ._models_py3 import NetworkConfiguration
    from ._models_py3 import NetworkSecurityGroupRule
    from ._models_py3 import NFSMountConfiguration
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import Pool
    from ._models_py3 import PoolEndpointConfiguration
    from ._models_py3 import ProxyResource
    from ._models_py3 import ResizeError
    from ._models_py3 import ResizeOperationStatus
    from ._models_py3 import Resource
    from ._models_py3 import ResourceFile
    from ._models_py3 import ScaleSettings
    from ._models_py3 import StartTask
    from ._models_py3 import TaskContainerSettings
    from ._models_py3 import TaskSchedulingPolicy
    from ._models_py3 import UserAccount
    from ._models_py3 import UserIdentity
    from ._models_py3 import VirtualMachineConfiguration
    from ._models_py3 import VirtualMachineFamilyCoreQuota
    from ._models_py3 import WindowsConfiguration
    from ._models_py3 import WindowsUserConfiguration
except (SyntaxError, ImportError):
    from ._models import ActivateApplicationPackageParameters
    from ._models import Application
    from ._models import ApplicationPackage
    from ._models import ApplicationPackageReference
    from ._models import AutoScaleRun
    from ._models import AutoScaleRunError
    from ._models import AutoScaleSettings
    from ._models import AutoStorageBaseProperties
    from ._models import AutoStorageProperties
    from ._models import AutoUserSpecification
    from ._models import AzureBlobFileSystemConfiguration
    from ._models import AzureFileShareConfiguration
    from ._models import BatchAccount
    from ._models import BatchAccountCreateParameters
    from ._models import BatchAccountKeys
    from ._models import BatchAccountRegenerateKeyParameters
    from ._models import BatchAccountUpdateParameters
    from ._models import BatchLocationQuota
    from ._models import Certificate
    from ._models import CertificateBaseProperties
    from ._models import CertificateCreateOrUpdateParameters
    from ._models import CertificateReference
    from ._models import CheckNameAvailabilityParameters
    from ._models import CheckNameAvailabilityResult
    from ._models import CIFSMountConfiguration
    from ._models import CloudServiceConfiguration
    from ._models import ContainerConfiguration
    from ._models import ContainerRegistry
    from ._models import DataDisk
    from ._models import DeleteCertificateError
    from ._models import DeploymentConfiguration
    from ._models import EnvironmentSetting
    from ._models import FixedScaleSettings
    from ._models import ImageReference
    from ._models import InboundNatPool
    from ._models import KeyVaultReference
    from ._models import LinuxUserConfiguration
    from ._models import MetadataItem
    from ._models import MountConfiguration
    from ._models import NetworkConfiguration
    from ._models import NetworkSecurityGroupRule
    from ._models import NFSMountConfiguration
    from ._models import Operation
    from ._models import OperationDisplay
    from ._models import Pool
    from ._models import PoolEndpointConfiguration
    from ._models import ProxyResource
    from ._models import ResizeError
    from ._models import ResizeOperationStatus
    from ._models import Resource
    from ._models import ResourceFile
    from ._models import ScaleSettings
    from ._models import StartTask
    from ._models import TaskContainerSettings
    from ._models import TaskSchedulingPolicy
    from ._models import UserAccount
    from ._models import UserIdentity
    from ._models import VirtualMachineConfiguration
    from ._models import VirtualMachineFamilyCoreQuota
    from ._models import WindowsConfiguration
    from ._models import WindowsUserConfiguration
from ._paged_models import ApplicationPackagePaged
from ._paged_models import ApplicationPaged
from ._paged_models import BatchAccountPaged
from ._paged_models import CertificatePaged
from ._paged_models import OperationPaged
from ._paged_models import PoolPaged
from ._batch_management_client_enums import (
    PoolAllocationMode,
    ProvisioningState,
    AccountKeyType,
    PackageState,
    CertificateFormat,
    CertificateProvisioningState,
    PoolProvisioningState,
    AllocationState,
    CachingType,
    StorageAccountType,
    ComputeNodeDeallocationOption,
    InterNodeCommunicationState,
    InboundEndpointProtocol,
    NetworkSecurityGroupRuleAccess,
    ComputeNodeFillType,
    ElevationLevel,
    LoginMode,
    AutoUserScope,
    ContainerWorkingDirectory,
    CertificateStoreLocation,
    CertificateVisibility,
    NameAvailabilityReason,
)

__all__ = [
    'ActivateApplicationPackageParameters',
    'Application',
    'ApplicationPackage',
    'ApplicationPackageReference',
    'AutoScaleRun',
    'AutoScaleRunError',
    'AutoScaleSettings',
    'AutoStorageBaseProperties',
    'AutoStorageProperties',
    'AutoUserSpecification',
    'AzureBlobFileSystemConfiguration',
    'AzureFileShareConfiguration',
    'BatchAccount',
    'BatchAccountCreateParameters',
    'BatchAccountKeys',
    'BatchAccountRegenerateKeyParameters',
    'BatchAccountUpdateParameters',
    'BatchLocationQuota',
    'Certificate',
    'CertificateBaseProperties',
    'CertificateCreateOrUpdateParameters',
    'CertificateReference',
    'CheckNameAvailabilityParameters',
    'CheckNameAvailabilityResult',
    'CIFSMountConfiguration',
    'CloudServiceConfiguration',
    'ContainerConfiguration',
    'ContainerRegistry',
    'DataDisk',
    'DeleteCertificateError',
    'DeploymentConfiguration',
    'EnvironmentSetting',
    'FixedScaleSettings',
    'ImageReference',
    'InboundNatPool',
    'KeyVaultReference',
    'LinuxUserConfiguration',
    'MetadataItem',
    'MountConfiguration',
    'NetworkConfiguration',
    'NetworkSecurityGroupRule',
    'NFSMountConfiguration',
    'Operation',
    'OperationDisplay',
    'Pool',
    'PoolEndpointConfiguration',
    'ProxyResource',
    'ResizeError',
    'ResizeOperationStatus',
    'Resource',
    'ResourceFile',
    'ScaleSettings',
    'StartTask',
    'TaskContainerSettings',
    'TaskSchedulingPolicy',
    'UserAccount',
    'UserIdentity',
    'VirtualMachineConfiguration',
    'VirtualMachineFamilyCoreQuota',
    'WindowsConfiguration',
    'WindowsUserConfiguration',
    'BatchAccountPaged',
    'ApplicationPackagePaged',
    'ApplicationPaged',
    'OperationPaged',
    'CertificatePaged',
    'PoolPaged',
    'PoolAllocationMode',
    'ProvisioningState',
    'AccountKeyType',
    'PackageState',
    'CertificateFormat',
    'CertificateProvisioningState',
    'PoolProvisioningState',
    'AllocationState',
    'CachingType',
    'StorageAccountType',
    'ComputeNodeDeallocationOption',
    'InterNodeCommunicationState',
    'InboundEndpointProtocol',
    'NetworkSecurityGroupRuleAccess',
    'ComputeNodeFillType',
    'ElevationLevel',
    'LoginMode',
    'AutoUserScope',
    'ContainerWorkingDirectory',
    'CertificateStoreLocation',
    'CertificateVisibility',
    'NameAvailabilityReason',
]
