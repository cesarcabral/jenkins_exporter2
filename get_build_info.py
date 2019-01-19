import requests

def get_build_info(self, job_name, build=None):
    build_number = str(build) if build else 'lastBuild'
    print("Getting build info.....#{}".format(build_number))

    path = self.get_path_from_job_name(job_name) + build_number + "/api/json"
    # print(path)

    response = requests.get(self.base_url + path, headers=self.defaultHeader, verify=self.ssl_verify)
    if response.status_code != 201 and response.status_code != 200:
        logging.error('Job \"{}:{}\" Not found.'.format(job_name,build_number))
        return None
    else:
        json_obj = response.json()
        return json_obj
