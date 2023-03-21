from ik import ManipJointState


class ManipParams:

    def from_dict(dict):
        result = ManipParams()
        link_dict = dict["links"]
        result._joint_names = link_dict["names"]
        result._joint_limits = link_dict["limits"]
        result._link_lengths = link_dict["lengths"]
        result._control_modes = dict["control_modes"]
        return result

    def joint_names(self):
        return self._joint_names

    def joint_limits(self):
        return self._joint_limits

    def link_lengths(self):
        return self._link_lengths

    def control_mode_params(self, name):
        return self._control_modes[name]


class ManipInterface:

    def get_jointstate(self) -> ManipJointState:
        pass

    def set_jointstate(self, jointstate: ManipJointState):
        pass

    def sleep(self, time):
        pass

    def get_manip_params(self) -> ManipParams:
        pass
