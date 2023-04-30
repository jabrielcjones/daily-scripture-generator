import json
import logging as logger
import pytest
import requests

ENDPOINT = "http://127.0.0.1"
PORT = "5000"


def remove_scripture(scripture):
    logger.info("Removing scripture...")

    ACTION = "scripture"

    payload = {"scripture": scripture}
    logger.debug(f"request payload: {payload}")

    response = requests.delete(f"{ENDPOINT}:{PORT}/{ACTION}", json=payload)

    content = json.loads(response.content)

    if not response.status_code == 200 or not content['success'] == "true":
        logger.error("Something went wrong while removing a scripture")
        logger.debug(f"Status Code: {response.status_code}")
        logger.debug(f"Success: {content['success']}")

    logger.info("Scripture removed")


def add_scripture(scripture):
    logger.info("Adding scripture...")

    ACTION = "scripture"

    payload = scripture
    logger.debug(f"request payload: {payload}")

    response = requests.post(f"{ENDPOINT}:{PORT}/{ACTION}", json=payload)

    content = json.loads(response.content)

    if not response.status_code == 200 or not content['success'] == "true":
        logger.error("Something went wrong while adding a scripture")
        logger.debug(f"Status Code: {response.status_code}")
        logger.debug(f"Success: {content['success']}")

    logger.info("Scripture added")


@pytest.fixture
def new_scripture():
    """
    """

    scripture = {
        "action": "test action",
        "verse": "test verse",
        "scripture": "test scripture"
    }

    logger.info("Test scripture formed...")
    yield scripture

    logger.info("Cleaning up...")
    remove_scripture(scripture['scripture'])


@pytest.fixture
def target_scripture():
    """
    """

    scripture = {
        "action": "test action",
        "verse": "test verse",
        "scripture": "test scripture"
    }

    add_scripture(scripture)

    logger.info("Test scripture added...")

    return scripture


def test_get_scripture():
    """
    """

    logger.info('Running GET SCRIPTURE test...')

    ACTION = "scripture"

    response = requests.get(f"{ENDPOINT}:{PORT}/{ACTION}")

    content = json.loads(response.content)

    logger.debug(f"assert {response.status_code} == 200")
    assert response.status_code == 200

    logger.debug(f"assert 'action' in {content.keys()}")
    assert "action" in content
    
    logger.debug(f"assert 'action' has value: {content['action']}")
    assert content['action']

    logger.debug(f"assert 'scripture' in {content.keys()}")
    assert "scripture" in content

    logger.debug(f"assert 'scripture' has value: {content['scripture']}")
    assert content['scripture']

    logger.debug(f"assert 'verse' in {content.keys()}")
    assert "verse" in content

    logger.debug(f"assert 'verse' has value: {content['verse']}")
    assert content['verse']


def test_post_scripture(new_scripture):
    """
    """

    logger.info('Running POST SCRIPTURE test...')

    ACTION = "scripture"

    payload = new_scripture
    logger.debug(f"request payload: {payload}")

    response = requests.post(f"{ENDPOINT}:{PORT}/{ACTION}", json=payload)

    logger.debug(f"assert {response.status_code} == 200")
    assert response.status_code == 200

    content = json.loads(response.content)
    logger.debug(f"assert {content['success']} == true")
    assert content['success'] == "true"


def test_delete_scripture(target_scripture):
    """
    """

    logger.info('Running DELETE SCRIPTURE test...')

    ACTION = "scripture"

    payload = target_scripture['scripture']
    logger.debug(f"request payload: {payload}")

    response = requests.delete(f"{ENDPOINT}:{PORT}/{ACTION}", json=payload)

    logger.debug(f"assert {response.status_code} == 200")
    assert response.status_code == 200

    content = json.loads(response.content)
    logger.debug(f"assert {content['success']} == true")
    assert content['success'] == "true"
