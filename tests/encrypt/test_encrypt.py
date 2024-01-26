from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("notsosecretmessage", "a")

    assert encrypt_message("notsosecretmessage", 2) == "egassemtercesost_on"

    assert encrypt_message("notsosecretmessage", 3) == "ton_egassemtercesos"

    assert encrypt_message("notsosecretmessage", 20) == "egassemtercesoston"
