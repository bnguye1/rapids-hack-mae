from pprintpp import pprint

import requests

headers = {
  "Content-Type":
  "application/json",
  #Auth Token
  "Authorization":
  "Bearer v2/user/eJwty0ELgjAUAOD/snOj9VS0bkUFRdsuA6mLPPecbWXF1FP035Po/PG92fC8NQ+2YmPfxPnFqCBLmeltO2jTZtILoWDvT+VBqPI8SLPptDneVdilMqwXbPZ7U++x93TFiFWHMeJr/FPlaVILlCKA4xbyhKdAjtcOiBeQYNHk1i0Fsc8XoyosZw=="
}


def get_dependencies(groupid, artifactid, version):

  try:
    #https://api.tidelift.com/external-api/v1/packages/maven/<PACKAGE>/releases/<VERSION>/dependencies
    url = f'https://api.tidelift.com/external-api/v1/packages/maven/{groupid}:{artifactid}/releases/{version}/dependencies'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
      data = response.json()

      # return list of dependencies
      return data["results"]
    else:
      print("Failed:", response.status_code)
  except requests.exceptions.RequestExceptions as e:
    print("Error:", str(e))


if __name__ == "__main__":
  response = get_dependencies("dom4j", "dom4j",
                              "1.6.1")

  pprint(response)
