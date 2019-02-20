from turbopy import Simulation, Module

class MyModule(Module):
    def __init__(self, owner, input_data):
        super().__init__(owner, input_data)
        print("MyModule Loaded: ", input_data["param"])
        self.x = input_data["param"]
    
    def reset(self):
        pass
    
    def update(self):
        print(self.owner.clock.time * self.x)

Module.add_module_to_library("MyModule", MyModule)

sim_config = {"Modules": [
        {"name": "MyModule",
         "param": 3.14,
         },
        {"name": "MyModule",
         "param": 22,
         },         
    ],
    "Grid": {},
    "Clock": {"start_time": 0,
              "end_time": 3}
    }
    
sim = Simulation(sim_config)
# sim.prepare_simulation()
sim.run()
