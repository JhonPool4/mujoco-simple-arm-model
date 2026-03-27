
from myosuite.envs.myo.myobase.reach_v0 import ReachEnvV0


class CustomEnv(ReachEnvV0):
  def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self._setup(**kwargs)
      self.mujoco_render_frames = True
      self.viewer_setup(azimuth=90,
                        elevation=-90,
                        distance=-1,
                        render_actuator=True,
                        render_tendon=True,
                        )