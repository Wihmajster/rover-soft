import math

class MotionInterpolator:
    def __init__(self, acceleration, max_velocity, max_error):
        self.acceleration = acceleration
        self.max_velocity = max_velocity

    def set_movement(self, start, end):
        self.direction = self._calculate_movement_vector(start, end)
        self.velocity = 0
        self.acceleration_distance = 0
        self.decceleration_distance = 0
        self.decceleration_velocity = 0
        self.accelerate = True
        self.deccelerate = False

        self.position = start
        self.end = end
        self.distance = self._calculate_distance(start, end)
    
    def _calculate_movement_vector(self, start, end):
        if len(start) != len(end):
            raise Exception("Cannot compare lists of different sizes!")
        vector = self._subtract_positions(start, end)
        return self._normalize_movement_vector(vector)
    
    def _subtract_positions(self, start, end):
        return [y-x for x, y in zip(start, end)]
        
    def _normalize_movement_vector(self, vector):
        norm = self._vector_norm(vector)
        return [x / norm for x in vector]
        
    def _vector_norm(self, vector):
        return math.sqrt(sum([x*x for x in vector]))

    def _calculate_distance(self, start, end):
        delta_vector = self._subtract_positions(start, end)
        return self._vector_norm(delta_vector)

    def movement_step(self, timestep):
        self._update_velocity(timestep)
        self._update_position(timestep)
        self.distance = self._calculate_distance(self.position, self.end)
        return self.position
    
    def _update_position(self, timestep):
        for x, direction in zip(self.position, self.direction):
            x += direction * self.velocity * timestep

    def _update_velocity(self, timestep):
        if self.accelerate:
            self._increment_velocity(timestep)
            self._increment_acceleration_distance(timestep)
            if self.velocity > self.max_velocity:
                self._stop_accelerating()
            if self.distance < self.acceleration_distance:
                self._stop_accelerating()
                self._start_deccelerating()
        if not self.accelerate and not self.deccelerate:
            if self.distance < self.acceleration_distance:
                self._start_deccelerating()
        if self.deccelerate:
            self._decrement_velocity(timestep)

    def _increment_velocity(self, timestep):
        self.velocity += self.acceleration * timestep

    def _increment_acceleration_distance(self, timestep):
        self.acceleration_distance += self.velocity * timestep

    def _decrement_velocity(self, timestep):
        self.velocity = self.decceleration_velocity * ((self.distance / self.decceleration_distance))**0.5
        
    def _stop_accelerating(self):
        self.accelerate = False
        if self.velocity > self.max_velocity:
            self.velocity = self.max_velocity
    
    def _start_deccelerating(self):
        self.deccelerate = True
        self.decceleration_distance = self.distance
        self.decceleration_velocity = self.velocity