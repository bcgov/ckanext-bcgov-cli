# Copyright  2015, Province of British Columbia
# License: https://github.com/bcgov/ckanext-bcgov/blob/master/license

from ckan.common import c, _

import logging
import re
import pylons.config as config
import ckan.lib.base as base
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from paste.deploy.converters import asbool
from routes.mapper import SubMapper


from ckanext.bcgov.util.util import (
    get_edc_tags,
    edc_type_label,
    get_state_values,
    get_username,
    get_user_orgs,
    get_orgs_user_can_edit,
    get_user_orgs_id,
    get_user_toporgs,
    get_organization_branches,
    can_view_resource,
    get_package_tracking,
    get_resource_tracking)

from ckanext.bcgov.util.helpers import (
    get_suborg_sector,
    get_user_dataset_num,
    get_package_data,
    is_license_open,
    get_record_type_label,
    get_suborgs,
    record_is_viewable,
    get_facets_selected,
    get_facets_unselected,
    get_sectors_list,
    get_dataset_type,
    get_organizations,
    get_organization_title,
    get_espg_id,
    get_edc_org,
    get_iso_topic_values,
    get_eas_login_url,
    get_fqdn,
    get_environment_name,
    get_version,
    get_bcgov_commit_id,
    resource_prefix,
    get_org_parent,
    size_or_link,
    display_pacific_time,
    sort_vocab_list,
    debug_full_info_as_list,
    remove_user_link,
    get_ofi_config,
    get_ofi_resources,
    get_non_ofi_resources,
    get_pow_config,
    log_this)


abort = base.abort

log = logging.getLogger('ckanext.bcgov.cli')
filter_query_regex = re.compile(r'([^:]+:"[^"]+"\s?)')


class SchemaPlugin(plugins.SingletonPlugin):

    plugins.implements(plugins.IConfigurer)

    plugins.implements(plugins.IRoutes, inherit=True)

    plugins.implements(plugins.ITemplateHelpers, inherit=False)

    plugins.implements(plugins.IPackageController, inherit=True)

    plugins.implements(plugins.IFacets, inherit=True)

    plugins.implements(plugins.IActions, inherit=True)

    plugins.implements(plugins.IAuthFunctions)

    plugins.implements(plugins.IResourceController, inherit=True)

    def get_helpers(self):
        return {
            "dataset_type": get_dataset_type,
            "edc_tags": get_edc_tags,
            "edc_orgs": get_organizations,
            "edc_org_branches": get_organization_branches,
            "edc_org_title": get_organization_title,
            "edc_type_label": edc_type_label,
            "edc_state_values": get_state_values,
            "edc_username": get_username,
            "get_sector": get_suborg_sector,
            "get_user_orgs": get_user_orgs,
            "get_user_orgs_id": get_user_orgs_id,
            "get_user_toporgs": get_user_toporgs,
            "get_suborg_sector": get_suborg_sector,
            "get_user_dataset_num": get_user_dataset_num,
            "get_edc_package": get_package_data,
            "is_license_open": is_license_open,
            "record_type_label": get_record_type_label,
            "get_suborgs": get_suborgs,
            "record_is_viewable": record_is_viewable,
            "get_espg_id": get_espg_id,
            "orgs_user_can_edit": get_orgs_user_can_edit,
            "get_facets_selected": get_facets_selected,
            "get_facets_unselected": get_facets_unselected,
            "get_sectors_list": get_sectors_list,
            "get_edc_org": get_edc_org,
            "get_iso_topic_values": get_iso_topic_values,
            "get_eas_login_url": get_eas_login_url,
            "get_fqdn": get_fqdn,
            "get_environment_name": get_environment_name,
            "get_version": get_version,
            "get_bcgov_commit_id": get_bcgov_commit_id,
            "googleanalytics_resource_prefix": resource_prefix,
            "get_parent_org": get_org_parent,
            "size_or_link": size_or_link,
            "display_pacific_time": display_pacific_time,
            "sort_vocab_list": sort_vocab_list,
            "debug_full_info_as_list": debug_full_info_as_list,
            "remove_user_link": remove_user_link,
            "get_ofi_config": get_ofi_config,
            "get_ofi_resources": get_ofi_resources,
            "get_non_ofi_resources": get_non_ofi_resources,
            "can_view_resource": can_view_resource,
            "get_pow_config": get_pow_config,
            "get_package_tracking": get_package_tracking,
            "get_resource_tracking": get_resource_tracking,
            "log": log_this
        }