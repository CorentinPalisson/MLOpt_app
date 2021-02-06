class FeaturesSet:
    def __init__(self):
        self.minimization = None

        self.dual_cost = None

        self.value_bound_difference = None

        self.value_root_actual_node_difference = None

        self.distance_nearest_integer = None
        self.distance_nearest_upper_integer = None

        self.integrality_gap = None

        self.actual_lower_bound = None
        self.global_lower_bound = None
        self.actual_upper_bound = None
        self.global_upper_bound = None

        self.lower_coefficient_objective = None
        self.upper_coefficient_objective = None

        self.min_degree_constraint_root = None
        self.max_degree_constraint_root = None
        self.mean_degree_constraint_root = None
        self.sd_degree_constraint_root = None

        self.min_variable_improve_rate = None
        self.max_variable_improve_rate = None
        self.mean_variable_improve_rate = None
        self.sd_variable_improve_rate = None
        self.first_quartile_variable_improve_rate = None
        self.third_quartile_improve_rate = None

        self.min_inv_sum_variables = None
        self.max_inv_sum_variables = None
        self.mean_inv_sum_variables = None
        self.sd_inv_sum_variables = None
        self.sum_inv_sum_variables = None

        self.min_inv_sum_variables_unfixed = None
        self.max_inv_sum_variables_unfixed = None
        self.mean_inv_sum_variables_unfixed = None
        self.sd_inv_sum_variables_unfixed = None
        self.sum_inv_sum_variables_unfixed = None

        self.min_unit_weight = None
        self.max_unit_weight = None
        self.mean_unit_weight = None
        self.sd_unit_weight = None
        self.sum_unit_weight = None

        self.mean_degree_constraint = None
        self.max_degree_constraint = None
        self.mean_degree_constraint = None
        self.sd_degree_constraint = None

        self.constraints_number = None
        self.negative_constraints_number = None
        self.positive_constraints_number = None

        self.solutions_number = None

        self.coefficients_number = None
        self.min_coefficient = None
        self.max_coefficient = None
        self.mean_coefficient = None
        self.sd_coefficient = None

        self.fractional_part = None

        self.lower_coefficient_to_variable = None
        self.upper_coefficient_to_variable = None

        self.min_positive_coefficient = None
        self.max_positive_coefficient = None
        self.min_negative_coefficient = None
        self.max_negative_coefficient = None

        self.weight_signed_variable = None
        self.weight_min_positive_coefficient = None
        self.weight_max_positive_coefficient = None
        self.weight_min_negative_coefficient = None
        self.weight_max_negative_coefficient = None

        self.depth_node = None

        self.lower_pseudo_cost = None  # Done : GatherControllCallBack
        self.upper_pseudo_cost = None  # Done : GatherControllCallBack

        self.ratio_pseudo_costs = None
        self.sum_pseudo_costs = None
        self.product_pseudo_costs = None

        self.up_driebreek_penalties = None
        self.down_driebreek_penalties = None

        self.estimated_objective_value = None

        self.actual_variable_improvement_rate = None

        self.detected_cuts_number = None

        self.lower_bound_after_cut = None

        self.upper_bound_after_cut = None

    def compute_all(self, model: Model, solver: Solver):
        pass

