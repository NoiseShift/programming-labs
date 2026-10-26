import sys
import utils.variant_mod as variant_mod


def main():
    if len(sys.argv) < 2:
        print("Использование: python main.py <координата>")
        return
    
    coord_to_check = float(sys.argv[1])

    path = [(10, 20, 0), (50, 60, 30), (100, 120, 50)]

    limits = {'x': (0, 200), 'y': (0, 200), 'z': (0, 100)}

    test_point = (coord_to_check, 100, 50)
    
    is_valid = variant_mod.validate_coordinates(test_point, limits)
    if is_valid:
        status = "допустима"
    else:
        status = "выход за границы"

    print(f"Проверка точки {test_point}: {status}")

    smoothed = variant_mod.smooth_trajectory(path)
    print(f"Сглаженная траектория: {smoothed}")

    reversed_path = variant_mod.get_reversed_path(path)

    print("=== ТРАЕКТОРИЯ РОБОТА-МАНИПУЛЯТОРА ===")
    print(f"Исходная траектория: {len(path)} точки")
    print(f"Обратный путь (срез [::-1]): {reversed_path}")


if __name__ == "__main__":
    main()