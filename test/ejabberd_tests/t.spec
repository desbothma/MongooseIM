{suites, "tests", ejabberdctl_SUITE}.
{config, ["test.config"]}.
{logdir, "ct_report"}.
{ct_hooks, [ct_tty_hook, ct_mongoose_hook]}.
%%To enable printing group and case enters on server side
%%{ct_hooks, [{ct_tty_hook, [print_group, print_case]}]}.
