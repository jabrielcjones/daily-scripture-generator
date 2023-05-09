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


def get_scripture():
    logger.info("Getting scripture...")

    ACTION = "scripture"

    response = requests.get(f"{ENDPOINT}:{PORT}/{ACTION}")

    content = json.loads(response.content)

    if not response.status_code == 200 or not content['success'] == "true":
        logger.error("Something went wrong while getting a scripture")
        logger.debug(f"Status Code: {response.status_code}")
        logger.debug(f"Success: {content['success']}")

    logger.info("Scripture retrieved")
    return content['scripture']


def update_verse(scripture, updated_verse):
    logger.info("Updating verse...")

    ACTION = "scripture/verse"

    payload = {"scripture": scripture, "updated_verse": updated_verse}
    logger.debug(f"request payload: {payload}")

    response = requests.update(f"{ENDPOINT}:{PORT}/{ACTION}")

    content = json.loads(response.content)

    if not response.status_code == 200 or not content['success'] == "true":
        logger.error("Something went wrong while updating a verse")
        logger.debug(f"Status Code: {response.status_code}")
        logger.debug(f"Success: {content['success']}")

    logger.info("Veruse updated")


@pytest.fixture
def fixture_add_scripture():
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
def fixture_delete_scripture():
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


@pytest.fixture
def fixture_update_scripture():
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


def test_post_scripture(fixture_add_scripture):
    """
    """

    logger.info('Running POST SCRIPTURE test...')

    ACTION = "scripture"

    payload = fixture_add_scripture
    logger.debug(f"request payload: {payload}")

    response = requests.post(f"{ENDPOINT}:{PORT}/{ACTION}", json=payload)

    logger.debug(f"assert {response.status_code} == 200")
    assert response.status_code == 200

    content = json.loads(response.content)
    logger.debug(f"assert {content['success']} == true")
    assert content['success'] == "true"


def test_delete_scripture(fixture_delete_scripture):
    """
    """

    logger.info('Running DELETE SCRIPTURE test...')

    ACTION = "scripture"

    payload = {"scripture": fixture_delete_scripture['scripture']}
    logger.debug(f"request payload: {payload}")

    response = requests.delete(f"{ENDPOINT}:{PORT}/{ACTION}", json=payload)

    logger.debug(f"assert {response.status_code} == 200")
    assert response.status_code == 200

    content = json.loads(response.content)
    logger.debug(f"assert {content['success']} == true")
    assert content['success'] == "true"


def test_update_scripture(fixture_update_scripture):
    """
    """

    logger.info('Running UPDATE SCRIPTURE test...')

    ACTION = "scripture/verse"

    payload = {
        "scripture": fixture_update_scripture['scripture'],
        "updated_verse": "updated test verse"
    }

    logger.debug(f"request payload: {payload}")

    response = requests.put(f"{ENDPOINT}:{PORT}/{ACTION}", json=payload)

    logger.debug(f"assert {response.status_code} == 200")
    assert response.status_code == 200

    content = json.loads(response.content)
    logger.debug(f"assert {content['success']} == true")
    assert content['success'] == "true"
