# This test code was written by the `hypothesis.extra.ghostwriter` module
# and is provided under the Creative Commons Zero public domain dedication.

import snakemake.sourcecache
from hypothesis import given, reject, strategies as st


@given(
    self=st.builds(snakemake.sourcecache.infer_source_file, st.text()).filter(
        lambda source_file: isinstance(
            source_file, snakemake.sourcecache.LocalSourceFile
        )
    )
)
def test_equivalent_SourceFile_get_cache_path_LocalSourceFile_get_cache_path(self):
    try:
        result_0_get_cache_path = snakemake.sourcecache.SourceFile.get_cache_path(
            self=self
        )
        result_1_get_cache_path = snakemake.sourcecache.LocalSourceFile.get_cache_path(
            self=self
        )
    except ValueError:
        reject()
    assert result_0_get_cache_path == result_1_get_cache_path, (
        result_0_get_cache_path,
        result_1_get_cache_path,
    )
