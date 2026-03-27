from gymnasium.envs.registration import register
register(
  id="myosuite_default_env-v0",
  entry_point="myosuite.envs.myo.myobase.reach_v0:ReachEnvV0",
  max_episode_steps=100_000,
  kwargs={
      "model_path": "./mujoco_envs/xml/simple_arm/elbow.xml",
      "target_reach_range": {
          "ee_site": ((0.2, 0.05, 0.20), (0.2, 0.05, 0.20)),
      },
      #"normalize_act": True,
      "frame_skip": 5,
  },  
)

register(
  id="custom_env-v0",
  entry_point="mujoco_envs.custom_env:CustomEnv",
  max_episode_steps=1000,
  kwargs={
      "model_path": "./mujoco_envs/xml/simple_arm/elbow.xml",
      "target_reach_range": {
          "ee_site": ((0.2, 0.05, 0.20), (0.2, 0.05, 0.20)),
      },
      #"normalize_act": True,
      "frame_skip": 1,
  },  
)