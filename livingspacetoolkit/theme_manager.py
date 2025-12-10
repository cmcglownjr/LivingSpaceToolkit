import os
import platform
import subprocess
from PySide6.QtWidgets import QApplication

def is_dark_mode():
    system = platform.system()

    # ----------------------
    # Linux KDE Plasma
    # ----------------------
    if system == "Linux":
        try:
            kde = subprocess.check_output(
                ["kreadconfig5", "--group", "KDE", "--key", "ColorScheme"],
                universal_newlines=True
            ).strip().lower()

            if "dark" in kde:
                return True
        except Exception:
            pass

        # GNOME detection
        try:
            gsettings = subprocess.check_output(
                ["gsettings", "get", "org.gnome.desktop.interface", "color-scheme"],
                universal_newlines=True
            ).strip()

            if "dark" in gsettings.lower():
                return True
        except Exception:
            pass

        return False

    # ----------------------
    # Windows 10/11
    # ----------------------
    if system == "Windows":
        try:
            import winreg
            key = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"
            )
            value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
            return value == 0
        except Exception:
            return False

    # ----------------------
    # macOS
    # ----------------------
    if system == "Darwin":
        try:
            result = subprocess.check_output(
                ["defaults", "read", "-g", "AppleInterfaceStyle"],
                stderr=subprocess.STDOUT
            ).decode().strip()

            if result.lower() == "dark":
                return True
        except Exception:
            pass

    return False


def apply_theme(app: QApplication):
    """Loads light or dark QSS depending on OS settings."""
    # TODO: Set first option to theme_dark.qss. Figure out how to properly switch between themes.
    theme_file = "Resource/theme_light.qss" if is_dark_mode() else "Resource/theme_light.qss"

    if os.path.exists(theme_file):
        with open(theme_file, "r") as f:
            app.setStyleSheet(f.read())
    else:
        print(f"Theme file not found: {theme_file}")
