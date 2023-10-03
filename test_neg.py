from sshcheckers import ssh_checkout_negativ

import yaml

with open("config.yaml") as f:
    data = yaml.safe_load(f)


class TestNegativ:

    def test_1_neg(self, make_folders, make_bad_files):
        # test1
        assert ssh_checkout_negativ(data['host'], data['user'], data['password'],
                                    f"cd {data['folder_out']}; 7z e {make_bad_files}", ""), "test_neg 1 FAIL"

    def test_2_neg(self, make_bad_files):
        # test2
        assert ssh_checkout_negativ(data['host'], data['user'], data['password'],
                                    f"cd {data['folder_out']}; 7z t arx2bad.7z", ""), "test_neg 2 FAIL"
