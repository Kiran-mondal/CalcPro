# CalcPro

A powerful calculator application built with Python and optimized C/C++ components via CMake.

## Overview

**CalcPro** is an advanced, feature-rich calculator that combines Python's flexibility with the performance of compiled C/C++ code. It provides both terminal-based and advanced computational capabilities.

## Technology Stack

- **Python**: 88.1% - Core application logic, CLI interface, and calculations
- **CMake**: 11.9% - Build system for C/C++ performance-critical components

## 🚀 Features

- ✅ Terminal-based interactive interface
- ✅ Basic arithmetic operations (Addition, Subtraction, Multiplication, Division)
- ✅ Advanced operations (Exponents, Square Roots)
- ✅ Input validation and error handling
- ✅ Continuous operation mode with graceful exit
- ✅ Lightweight and fast execution
- ✅ Cross-platform compatibility

## 🧮 Supported Operations

| Operation        | Description        |
|------------------|--------------------|
| Addition         | `a + b`            |
| Subtraction      | `a - b`            |
| Multiplication   | `a * b`            |
| Division         | `a / b`            |
| Power (x^y)      | `pow(x, y)`        |
| Square Root      | `sqrt(x)`          |

## 📋 Prerequisites

- **Python** 3.7 or higher
- **CMake** 3.10 or higher
- **C/C++ Compiler** (GCC, Clang, or MSVC)

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Kiran-mondal/CalcPro.git
cd CalcPro
```

### 2. Build the Project

```bash
mkdir build
cd build
cmake ..
make
```

### 3. Install Python Dependencies (if applicable)

```bash
pip install -r requirements.txt
```

## 💻 Usage

### Running the Calculator

```bash
python calcpro.py
```

Or if compiled:

```bash
./calcpro
```

### Example Session

```
Welcome to CalcPro!
Select an operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Power
6. Square Root
7. Exit

Enter your choice (1-7): 1
Enter first number: 10
Enter second number: 20
Result: 30
```

## 📂 Project Structure

```
CalcPro/
├── src/                  # Source code files
│   └── calcpro.py       # Main calculator application
├── build/               # Build directory (generated)
├── CMakeLists.txt       # CMake configuration
├── requirements.txt     # Python dependencies
├── LICENSE              # MIT License
└── README.md            # This file
```

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🐛 Issues & Support

- **Found a bug?** Open an [issue](https://github.com/Kiran-mondal/CalcPro/issues)
- **Have a question?** Check [Discussions](https://github.com/Kiran-mondal/CalcPro/discussions)
- **Want to contribute?** Submit a [Pull Request](https://github.com/Kiran-mondal/CalcPro/pulls)

## 👨‍💻 Author

**Kiran Mondal**
- GitHub: [@Kiran-mondal](https://github.com/Kiran-mondal)

## 📊 Project Info

| Detail | Value |
|--------|-------|
| **Created** | April 29, 2025 |
| **Last Updated** | June 2, 2026 |
| **Primary Language** | Python (88.1%) |
| **Build System** | CMake (11.9%) |
| **License** | MIT |
| **Status** | Active |

---

**Made with ❤️ by Kiran-mondal**

For more information, visit the [repository](https://github.com/Kiran-mondal/CalcPro).
