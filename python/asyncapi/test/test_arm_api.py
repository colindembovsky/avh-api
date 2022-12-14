# coding: utf-8

"""
    Arm API

    REST API to manage your virtual devices.  # noqa: E501

    The version of the OpenAPI document: 3.15.0-15704
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import avh_api_async
from avh_api_async.api.arm_api import ArmApi  # noqa: E501
from avh_api_async.rest import ApiException


class TestArmApi(unittest.TestCase):
    """ArmApi unit test stubs"""

    def setUp(self):
        self.api = avh_api_async.api.arm_api.ArmApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_trial_status(self):
        """Test case for trial_status

        Get Trial Status  # noqa: E501
        """
        pass

    def test_v1_add_project_key(self):
        """Test case for v1_add_project_key

        Add Project Authorized Key  # noqa: E501
        """
        pass

    def test_v1_add_team_role_to_project(self):
        """Test case for v1_add_team_role_to_project

        Add team role to project  # noqa: E501
        """
        pass

    def test_v1_add_user_role_to_project(self):
        """Test case for v1_add_user_role_to_project

        Add user role to project  # noqa: E501
        """
        pass

    def test_v1_add_user_to_team(self):
        """Test case for v1_add_user_to_team

        Add user to team  # noqa: E501
        """
        pass

    def test_v1_auth_login(self):
        """Test case for v1_auth_login

        Log In  # noqa: E501
        """
        pass

    def test_v1_btrace_preauthorize(self):
        """Test case for v1_btrace_preauthorize

        Pre-authorize an btrace download  # noqa: E501
        """
        pass

    def test_v1_clear_core_trace(self):
        """Test case for v1_clear_core_trace

        Clear CoreTrace logs  # noqa: E501
        """
        pass

    def test_v1_clear_hyper_trace(self):
        """Test case for v1_clear_hyper_trace

        Clear HyperTrace logs  # noqa: E501
        """
        pass

    def test_v1_clear_hyper_trace_hooks(self):
        """Test case for v1_clear_hyper_trace_hooks

        Clear Hooks on an instance  # noqa: E501
        """
        pass

    def test_v1_clear_instance_panics(self):
        """Test case for v1_clear_instance_panics

        Clear Panics  # noqa: E501
        """
        pass

    def test_v1_create_hook(self):
        """Test case for v1_create_hook

        Create hypervisor hook for Instance  # noqa: E501
        """
        pass

    def test_v1_create_image(self):
        """Test case for v1_create_image

        Create a new Image  # noqa: E501
        """
        pass

    def test_v1_create_instance(self):
        """Test case for v1_create_instance

        Create Instance  # noqa: E501
        """
        pass

    def test_v1_create_project(self):
        """Test case for v1_create_project

        Create a Project  # noqa: E501
        """
        pass

    def test_v1_create_snapshot(self):
        """Test case for v1_create_snapshot

        Create Instance Snapshot  # noqa: E501
        """
        pass

    def test_v1_create_subscriber_invite(self):
        """Test case for v1_create_subscriber_invite

        Create Subscriber Invite  # noqa: E501
        """
        pass

    def test_v1_delete_hook(self):
        """Test case for v1_delete_hook

        Delete an existing hypervisor hook  # noqa: E501
        """
        pass

    def test_v1_delete_image(self):
        """Test case for v1_delete_image

        Delete Image  # noqa: E501
        """
        pass

    def test_v1_delete_instance(self):
        """Test case for v1_delete_instance

        Remove Instance  # noqa: E501
        """
        pass

    def test_v1_delete_instance_snapshot(self):
        """Test case for v1_delete_instance_snapshot

        Delete a Snapshot  # noqa: E501
        """
        pass

    def test_v1_delete_project(self):
        """Test case for v1_delete_project

        Delete a Project  # noqa: E501
        """
        pass

    def test_v1_delete_snapshot(self):
        """Test case for v1_delete_snapshot

        Delete a Snapshot  # noqa: E501
        """
        pass

    def test_v1_disable_expose_port(self):
        """Test case for v1_disable_expose_port

        Disable an exposed port on an instance for device access.  # noqa: E501
        """
        pass

    def test_v1_enable_expose_port(self):
        """Test case for v1_enable_expose_port

        Enable an exposed port on an instance for device access.  # noqa: E501
        """
        pass

    def test_v1_execute_hyper_trace_hooks(self):
        """Test case for v1_execute_hyper_trace_hooks

        Execute Hooks on an instance  # noqa: E501
        """
        pass

    def test_v1_get_hook_by_id(self):
        """Test case for v1_get_hook_by_id

        Get hypervisor hook by id  # noqa: E501
        """
        pass

    def test_v1_get_hooks(self):
        """Test case for v1_get_hooks

        Get all hypervisor hooks for Instance  # noqa: E501
        """
        pass

    def test_v1_get_image(self):
        """Test case for v1_get_image

        Get Image Metadata  # noqa: E501
        """
        pass

    def test_v1_get_images(self):
        """Test case for v1_get_images

        Get all Images Metadata  # noqa: E501
        """
        pass

    def test_v1_get_instance(self):
        """Test case for v1_get_instance

        Get Instance  # noqa: E501
        """
        pass

    def test_v1_get_instance_console(self):
        """Test case for v1_get_instance_console

        Get console websocket URL  # noqa: E501
        """
        pass

    def test_v1_get_instance_console_log(self):
        """Test case for v1_get_instance_console_log

        Get Console Log  # noqa: E501
        """
        pass

    def test_v1_get_instance_gpios(self):
        """Test case for v1_get_instance_gpios

        Get Instance GPIOs  # noqa: E501
        """
        pass

    def test_v1_get_instance_panics(self):
        """Test case for v1_get_instance_panics

        Get Panics  # noqa: E501
        """
        pass

    def test_v1_get_instance_peripherals(self):
        """Test case for v1_get_instance_peripherals

        Get Instance Peripherals  # noqa: E501
        """
        pass

    def test_v1_get_instance_quick_connect_command(self):
        """Test case for v1_get_instance_quick_connect_command

        Recommended SSH Command for Quick Connect  # noqa: E501
        """
        pass

    def test_v1_get_instance_screenshot(self):
        """Test case for v1_get_instance_screenshot

        Get Instance Screenshot  # noqa: E501
        """
        pass

    def test_v1_get_instance_snapshot(self):
        """Test case for v1_get_instance_snapshot

        Get Instance Snapshot  # noqa: E501
        """
        pass

    def test_v1_get_instance_snapshots(self):
        """Test case for v1_get_instance_snapshots

        Get Instance Snapshots  # noqa: E501
        """
        pass

    def test_v1_get_instance_state(self):
        """Test case for v1_get_instance_state

        Get state of Instance  # noqa: E501
        """
        pass

    def test_v1_get_instances(self):
        """Test case for v1_get_instances

        Get Instances  # noqa: E501
        """
        pass

    def test_v1_get_model_software(self):
        """Test case for v1_get_model_software

        Get Software for Model  # noqa: E501
        """
        pass

    def test_v1_get_models(self):
        """Test case for v1_get_models

        Get Supported Models  # noqa: E501
        """
        pass

    def test_v1_get_project(self):
        """Test case for v1_get_project

        Get a Project  # noqa: E501
        """
        pass

    def test_v1_get_project_instances(self):
        """Test case for v1_get_project_instances

        Get Instances in Project  # noqa: E501
        """
        pass

    def test_v1_get_project_keys(self):
        """Test case for v1_get_project_keys

        Get Project Authorized Keys  # noqa: E501
        """
        pass

    def test_v1_get_project_vpn_config(self):
        """Test case for v1_get_project_vpn_config

        Get Project VPN Configuration  # noqa: E501
        """
        pass

    def test_v1_get_projects(self):
        """Test case for v1_get_projects

        Get Projects  # noqa: E501
        """
        pass

    def test_v1_get_snapshot(self):
        """Test case for v1_get_snapshot

        Get Snapshot  # noqa: E501
        """
        pass

    def test_v1_kcrange(self):
        """Test case for v1_kcrange

        Get Kernel extension ranges  # noqa: E501
        """
        pass

    def test_v1_list_threads(self):
        """Test case for v1_list_threads

        Get Running Threads (CoreTrace)  # noqa: E501
        """
        pass

    def test_v1_media_play(self):
        """Test case for v1_media_play

        Start playing media  # noqa: E501
        """
        pass

    def test_v1_media_stop(self):
        """Test case for v1_media_stop

        Stop playing media  # noqa: E501
        """
        pass

    def test_v1_patch_instance(self):
        """Test case for v1_patch_instance

        Update Instance  # noqa: E501
        """
        pass

    def test_v1_pause_instance(self):
        """Test case for v1_pause_instance

        Pause an Instance  # noqa: E501
        """
        pass

    def test_v1_post_instance_input(self):
        """Test case for v1_post_instance_input

        Provide Instance Input  # noqa: E501
        """
        pass

    def test_v1_ready(self):
        """Test case for v1_ready

        API Status  # noqa: E501
        """
        pass

    def test_v1_reboot_instance(self):
        """Test case for v1_reboot_instance

        Reboot an Instance  # noqa: E501
        """
        pass

    def test_v1_remove_project_key(self):
        """Test case for v1_remove_project_key

        Delete Project Authorized Key  # noqa: E501
        """
        pass

    def test_v1_remove_team_role_from_project(self):
        """Test case for v1_remove_team_role_from_project

        Remove team role from project  # noqa: E501
        """
        pass

    def test_v1_remove_user_from_team(self):
        """Test case for v1_remove_user_from_team

        Remove user from team  # noqa: E501
        """
        pass

    def test_v1_remove_user_role_from_project(self):
        """Test case for v1_remove_user_role_from_project

        Remove user role from project  # noqa: E501
        """
        pass

    def test_v1_rename_instance_snapshot(self):
        """Test case for v1_rename_instance_snapshot

        Rename a Snapshot  # noqa: E501
        """
        pass

    def test_v1_restore_instance_snapshot(self):
        """Test case for v1_restore_instance_snapshot

        Restore a Snapshot  # noqa: E501
        """
        pass

    def test_v1_roles(self):
        """Test case for v1_roles

        Get all roles  # noqa: E501
        """
        pass

    def test_v1_set_instance_gpios(self):
        """Test case for v1_set_instance_gpios

        Set Instance GPIOs  # noqa: E501
        """
        pass

    def test_v1_set_instance_peripherals(self):
        """Test case for v1_set_instance_peripherals

        Set Instance Peripherals  # noqa: E501
        """
        pass

    def test_v1_set_instance_state(self):
        """Test case for v1_set_instance_state

        Set state of Instance  # noqa: E501
        """
        pass

    def test_v1_snapshot_rename(self):
        """Test case for v1_snapshot_rename

        Rename a Snapshot  # noqa: E501
        """
        pass

    def test_v1_start_core_trace(self):
        """Test case for v1_start_core_trace

        Start CoreTrace on an instance  # noqa: E501
        """
        pass

    def test_v1_start_hyper_trace(self):
        """Test case for v1_start_hyper_trace

        Start HyperTrace on an instance  # noqa: E501
        """
        pass

    def test_v1_start_instance(self):
        """Test case for v1_start_instance

        Start an Instance  # noqa: E501
        """
        pass

    def test_v1_start_network_monitor(self):
        """Test case for v1_start_network_monitor

        Start Network Monitor on an instance.  # noqa: E501
        """
        pass

    def test_v1_stop_core_trace(self):
        """Test case for v1_stop_core_trace

        Stop CoreTrace on an instance.  # noqa: E501
        """
        pass

    def test_v1_stop_hyper_trace(self):
        """Test case for v1_stop_hyper_trace

        Stop HyperTrace on an instance.  # noqa: E501
        """
        pass

    def test_v1_stop_instance(self):
        """Test case for v1_stop_instance

        Stop an Instance  # noqa: E501
        """
        pass

    def test_v1_stop_network_monitor(self):
        """Test case for v1_stop_network_monitor

        Stop Network Monitor on an instance.  # noqa: E501
        """
        pass

    def test_v1_team_change(self):
        """Test case for v1_team_change

        Update team  # noqa: E501
        """
        pass

    def test_v1_team_create(self):
        """Test case for v1_team_create

        Create team  # noqa: E501
        """
        pass

    def test_v1_team_delete(self):
        """Test case for v1_team_delete

        Delete team  # noqa: E501
        """
        pass

    def test_v1_teams(self):
        """Test case for v1_teams

        Get teams  # noqa: E501
        """
        pass

    def test_v1_unpause_instance(self):
        """Test case for v1_unpause_instance

        Unpause an Instance  # noqa: E501
        """
        pass

    def test_v1_update_hook(self):
        """Test case for v1_update_hook

        Update an existing hypervisor hook  # noqa: E501
        """
        pass

    def test_v1_update_project(self):
        """Test case for v1_update_project

        Update a Project  # noqa: E501
        """
        pass

    def test_v1_update_project_settings(self):
        """Test case for v1_update_project_settings

        Change Project Settings  # noqa: E501
        """
        pass

    def test_v1_upload_image_data(self):
        """Test case for v1_upload_image_data

        Upload Image Data  # noqa: E501
        """
        pass

    def test_v1_web_player_allowed_domains(self):
        """Test case for v1_web_player_allowed_domains

        Retrieve the list of allowed domains for all Web Player sessions  # noqa: E501
        """
        pass

    def test_v1_web_player_create_session(self):
        """Test case for v1_web_player_create_session

        Create a new Web Player Session  # noqa: E501
        """
        pass

    def test_v1_web_player_destroy_session(self):
        """Test case for v1_web_player_destroy_session

        Tear down a Web Player Session  # noqa: E501
        """
        pass

    def test_v1_web_player_list_sessions(self):
        """Test case for v1_web_player_list_sessions

        List all Web Player sessions  # noqa: E501
        """
        pass

    def test_v1_web_player_session_info(self):
        """Test case for v1_web_player_session_info

        Retrieve Web Player Session Information  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
