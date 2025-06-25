# 🏀 Ball Physics Engine

A simple yet powerful 2D physics simulation written in Python using Pygame.  
This project demonstrates core principles of Newtonian mechanics, including gravity, velocity, acceleration, and collision response with realistic energy loss. Users can interactively "throw" a ball using mouse input, and watch it bounce within a window using physics-based motion.

---

## 🚀 Features

- ✅ Real-time 2D motion using Euler integration & Kinematics
- ✅ Interactive mouse click-and-drag throw mechanism  
- ✅ Simulated gravity (constant vertical acceleration)  
- ✅ Wall and ground collision detection and response  
- ✅ Adjustable restitution coefficient (bounciness)

---

## 📸 Demo

Coming Soon!

---

## 🧠 Physics Concepts Used

- **Newton’s Second Law**:  
  Acceleration causes changes in velocity (`v += a * dt`) and displacement (`p += v * dt + 0.5 * a * dt * dt`)

- **Gravity Simulation**:  
  Constant downward acceleration (`a = 980 px/s²`)

- **Elastic Collisions**:  
  When the ball hits a surface, its velocity is reversed and scaled by a restitution factor

- **Mouse Impulse Control**:  
  Drag-and-release sets the velocity vector based on distance and direction of drag

