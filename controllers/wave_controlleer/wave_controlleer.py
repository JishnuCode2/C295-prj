from controller import Robot, Keyboard, Motion

robot = Robot()

wave = Motion("../../motions/wave.motion");

timestep = 32;

kb = Keyboard();
kb.enable(timestep);

print("Press Up Arrow to Wave");
key = -1;

while(robot.step(timestep) != -1):
    key = kb.getKey();
    
    if(key == Keyboard.UP):
        wave.play();
        