import pytest
from lesson_14.homework_14 import log_event

def test_log_event_success(caplog):
    log_event('Adam', 'success')
    assert len(caplog.records) == 1
    record = caplog.records[0]
    assert record.levelname == 'INFO'

def test_log_event_expired(caplog):
    log_event('Adam', 'expired')
    assert len(caplog.records) == 1
    record = caplog.records[0]
    assert record.levelname == 'WARNING'

def test_log_event_error(caplog):
    log_event('Adam', 'error')
    assert len(caplog.records) == 1
    record = caplog.records[0]
    assert record.levelname == 'ERROR'