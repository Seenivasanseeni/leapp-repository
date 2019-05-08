from leapp.snactor.fixture import current_actor_context
from leapp.models import ActiveKernelModule, ActiveKernelModulesFacts
from leapp.reporting import Report


def create_modulesfacts(kernel_modules):
    return ActiveKernelModulesFacts(kernel_modules=kernel_modules)


def test_actor_with_btrfs_module(current_actor_context):
    with_btrfs = [
        ActiveKernelModule(name='btrfs', parameters=[]),
        ActiveKernelModule(name='kvm', parameters=[])]

    current_actor_context.feed(create_modulesfacts(kernel_modules=with_btrfs))
    current_actor_context.run()
    assert 'inhibitor' in current_actor_context.consume(Report)[0].flags


def test_actor_without_btrfs_module(current_actor_context):
    without_btrfs = [
        ActiveKernelModule(name='kvm_intel', parameters=[]),
        ActiveKernelModule(name='kvm', parameters=[])]

    current_actor_context.feed(create_modulesfacts(kernel_modules=without_btrfs))
    current_actor_context.run()
    assert not current_actor_context.consume(Report)
