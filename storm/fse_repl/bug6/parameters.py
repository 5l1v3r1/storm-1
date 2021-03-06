bug_6_parameters = {
        "max_depth": 64,
        "max_assert": 64,
        "enrichment_steps": 1000,
        "number_of_mutants": 1000,
        "mutant_generation_timeout" : 900,
        "mutant_running_timeout" : 900,
        "solver_timeout" : 60,
        "check_sat_using" : ["no", "no"],
        "check_sat_using_options" : ["horn", "(then horn-simplify default)", "dom-simplify", "(then dom-simplify smt)"],
        "incremental": ["no", "no"],
        "theory" : "QF_BV",
        "buggy_mutant" : "mutant_217.smt2",
        "solver" : "z3",
        "solverbin" : "/home/numair/z3_versions/z3_da2f/bin/z3",
        "fixed_solverbin" : "/home/numair/z3_versions/z3_05da/bin/z3"
}


def get_bug6_parameters_dict():
    return bug_6_parameters
