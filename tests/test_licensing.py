"""Distribution consistency checks, not a legal enforceability assessment."""
from pathlib import Path
import hashlib
import tomllib

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills/codex-sol-claude-orchestrator'


def test_skill_legal_files_match_root():
    for name in ['LICENSE', 'NOTICE']:
        assert (ROOT / name).read_text(encoding='utf-8') == (SKILL / name).read_text(encoding='utf-8')


def test_package_license_and_version_are_explicit():
    project = tomllib.loads((ROOT / 'pyproject.toml').read_text(encoding='utf-8'))['project']
    assert project['license'] == 'LicenseRef-Xiaoye-NC-Reciprocal-2.0'
    assert project['version'] == '0.4.1'
    assert 'LICENSE' in project['license-files']
    assert 'NOTICE' in project['license-files']
    for name in ['mcp-MIT.txt', 'claude-agent-sdk-MIT.txt']:
        text = (ROOT / 'docs/third-party-licenses' / name).read_text(encoding='utf-8')
        assert 'MIT License' in text


def test_legacy_license_is_preserved():
    text = (ROOT / 'docs/license-history/ncrs-1.0.txt').read_text(encoding='utf-8')
    assert hashlib.sha256(text.encode()).hexdigest() == '546bdce33e889eac232ef2dd22682b870423288f280380de47dabc9b314251c3'
