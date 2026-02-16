# Sound Wave Drainage Expert / 声波排水专家

This is a web-based utility application designed to help expel water from device speakers using sound frequency vibrations. It is served via a lightweight Flask server.

这是一个基于 Web 的实用应用程序，旨在利用声波频率振动帮助排出设备扬声器中的水分。该应用通过轻量级的 Flask 服务器运行。

## Features / 功能特点

- **Variable Frequency Tone / 可变频率音调**  
  Generates adjustable sound waves ranging from 100Hz to 800Hz using the Web Audio API to effectively vibrate water out of speaker grills.  
  利用 Web Audio API 产生 100Hz 到 800Hz 的可调节声波，有效震动并排出扬声器格栅中的水分。

- **Visual Feedback / 视觉反馈**  
  Interactive water wave animations providing visual operational status.  
  提供直观的交互式水波动画，展示当前的运行状态。

- **Simple Controls / 简单控制**  
  One-button start/stop interface with a precision slider for frequency adjustment.  
  一键启动/停止的极简界面，并配有用于微调频率的精密滑块。

- **Mobile Optimized / 移动端优化**  
  Response design specifically tailored for mobile devices, including safe-area support and touch-friendly controls.  
  专为移动设备打造的响应式设计，适配屏幕安全区域并提供友好的触控体验。

## How to Run / 如何运行

### Prerequisites / 前置要求
- Python 3.x

### Quick Start / 快速开始

1. **Install Dependencies / 安装依赖**:
   ```bash
   pip3 install -r requirements.txt
   ```

2. **Start the Application / 启动应用**:
   ```bash
   python3 app.py
   ```
   
   *Alternatively, you can use the provided shell script:*  
   *或者，您可以使用提供的 shell 脚本：*
   ```bash
   chmod +x run.sh
   ./run.sh
   ```

3. **Access the App / 访问应用**:
   Open `http://localhost:5000` in your web browser.  
   请在浏览器中访问 `http://localhost:5000`。

## Usage Tips / 使用建议

- **Maximize Volume**: Turn your device volume to the maximum level for the best vibration effect.  
  **调大音量**：将设备音量调至最大，以获得最佳的震动排水效果。
  
- **Positioning**: Place the device with the speaker facing downwards to let gravity assist the drainage.  
  **放置姿势**：建议将设备的扬声器朝下放置，利用重力辅助排水。
