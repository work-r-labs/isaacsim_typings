from __future__ import annotations
__all__ = ['cache_kernels', 'cuda_output', 'enable_backward', 'enable_graph_capture_module_load_by_default', 'enable_mempools_at_init', 'kernel_cache_dir', 'llvm_cuda', 'max_unroll', 'mode', 'print_launches', 'ptx_target_arch', 'quiet', 'verbose', 'verbose_warnings', 'verify_autograd_array_access', 'verify_cuda', 'verify_fp', 'version']
cache_kernels: bool = True
cuda_output = None
enable_backward: bool = False
enable_graph_capture_module_load_by_default: bool = True
enable_mempools_at_init: bool = True
kernel_cache_dir: str = '/home/chris/.cache/warp/1.5.0'
llvm_cuda: bool = False
max_unroll: int = 16
mode: str = 'release'
print_launches: bool = False
ptx_target_arch: int = 75
quiet: bool = False
verbose: bool = False
verbose_warnings: bool = False
verify_autograd_array_access: bool = False
verify_cuda: bool = False
verify_fp: bool = False
version: str = '1.5.0'
