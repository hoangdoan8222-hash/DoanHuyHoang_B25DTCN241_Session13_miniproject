parking_lot = [
    {"id": 1, "plate": "29A-12345", "type": 1, "entry_time": 8},
    {"id": 2, "plate": "30K-99999", "type": 2, "entry_time": 10}
]

next_id = 3
while True:
    print("\n===== SMART PARKING SYSTEM =====")
    print("1. Check-in (Nhận xe vào bãi)")
    print("2. Báo cáo tồn kho (Danh sách xe trong bãi)")
    print("3. Tìm kiếm xe theo biển số")
    print("4. Check-out (Tính phí và trả xe)")
    print("5. Thoát chương trình")
    print("================================")
    
    choice = input("Chọn chức năng (1-5): ").strip()
    match choice:
        case "1":
            print("\n--- THỰC HIỆN CHỨC NĂNG: CHECK-IN ---")
            plate = input("Nhập biển số xe: ").strip().upper()
            if plate == "":
                print("[Lỗi]: Biển số xe không được để trống!")
                continue
            is_duplicate = False
            for vehicle in parking_lot:
                if vehicle["plate"] == plate:
                    is_duplicate = True
                    break
            if is_duplicate:
                print("[Lỗi]: Xe với biển số này đã tồn tại trong bãi!")  
                continue
            
            vehicle_type = 0
            while True:
                print("Chọn loại xe (1: Xe máy, 2: Ô tô)")
                type_input = input("Nhập lựa chọn: ").strip()
                if type_input == "1" or type_input == "2":
                    vehicle_type = int(type_input)
                    break
                else:
                    print("[Lỗi]: Loại xe không hợp lệ (1: Xe máy, 2: Ô tô)!")  
            
            entry_time = 0
            while True:
                entry_time_str = input("Nhập giờ vào bãi (0-24): ").strip()
                if entry_time_str.isdigit():
                    entry_time = int(entry_time_str)
                    if 0 <= entry_time <= 24:
                        break
                print("[Lỗi]: Giờ vào không hợp lệ! Vui lòng nhập số nguyên từ 0 đến 24.")
            new_vehicle = {
                "id": next_id,
                "plate": plate,
                "type": vehicle_type,
                "entry_time": entry_time
            }
            parking_lot.append(new_vehicle)
            next_id += 1 
            print(f"[Thành công]: Xe [{plate}] đã được đăng ký vào bãi với ID {new_vehicle['id']}.")

        case "2":
            print("\n--- BÁO CÁO TỒN KHO PHƯƠNG TIỆN ---")
            if len(parking_lot) == 0:
                print("[Thông báo: Bãi xe hiện đang trống!]")
            else:
                print("-" * 60)
                print(f"{'ID':<6} | {'Biển số xe':<15} | {'Loại xe':<12} | {'Giờ vào (h)':<12}")
                print("-" * 60)
                for vehicle in parking_lot:
                    type_name = "Xe máy" if vehicle["type"] == 1 else "Ô tô"
                    print(f"{vehicle['id']:<6} | {vehicle['plate']:<15} | {type_name:<12} | {vehicle['entry_time']:<12}")
                print("-" * 60)
                print(f"Tổng số xe đang đỗ (Trạng thái parked): {len(parking_lot)}")

        case "3":
            print("\n--- TÌM KIẾM THÔNG TIN PHƯƠNG TIỆN ---")
            search_plate = input("Nhập biển số xe cần tìm: ").strip().upper()
            
            if search_plate == "":
                print("[Lỗi]: Dữ liệu tra cứu không được để trống!")
                continue
            found_vehicle = None
            for vehicle in parking_lot:
                if vehicle["plate"] == search_plate:
                    found_vehicle = vehicle
                    break
            if found_vehicle is not None:
                print("-> [KẾT QUẢ TÌM THẤY]:")
                print(found_vehicle)
            else:
                print(f"[Lỗi]: Không tìm thấy biển số [{search_plate}] trong hệ thống!") 

        case "4":
            print("\n--- THỰC HIỆN CHỨC NĂNG: CHECK-OUT ---")
            checkout_plate = input("Nhập biển số xe muốn xuất bãi: ").strip().upper()
            if checkout_plate == "":
                print("[Lỗi]: Biển số xe không được để trống!")
                continue
            found_index = -1
            for i in range(len(parking_lot)):
                if parking_lot[i]["plate"] == checkout_plate:
                    found_index = i
                    break
            if found_index == -1:
                print(f"[Lỗi]: Không tìm thấy biển số [{checkout_plate}] trong hệ thống!")  
                continue
            vehicle_target = parking_lot[found_index]
            exit_time = 0
            
            while True:
                exit_time_str = input(f"Nhập giờ ra bãi (Giờ vào: {vehicle_target['entry_time']}h): ").strip()
                
                if exit_time_str.isdigit():
                    exit_time = int(exit_time_str)
                    if 0 <= exit_time <= 24:
                        if exit_time >= vehicle_target["entry_time"]:
                            break
                        else:
                            print("[Lỗi]: Giờ ra phải sau hoặc bằng giờ vào!")  
                            continue
                print("[Lỗi]: Giờ ra không hợp lệ! Vui lòng nhập số nguyên từ 0 đến 24.")
            duration = exit_time - vehicle_target["entry_time"]
            unit_price = 5000 if vehicle_target["type"] == 1 else 20000 
            total_fee = duration * unit_price

            print("\n--- HÓA ĐƠN XUẤT BÃI ---")
            print(f"ID phương tiện: {vehicle_target['id']}")
            print(f"Biển số xe:    {vehicle_target['plate']}")
            print(f"Thời gian đỗ:  {duration} tiếng ({vehicle_target['entry_time']}h -> {exit_time}h)")
            print(f"Thành tiền:     {total_fee:,} VND")
            print("------------------------")
            
            parking_lot.pop(found_index)
            print(f"[Thành công]: Xe [{checkout_plate}] đã thanh toán và rời khỏi bãi.")

        case "5":
            print("\nHệ thống đang đóng. Cảm ơn bạn đã sử dụng Smart Parking System!")
            break

        case _:
            print("[Lỗi]: Lựa chọn không hợp lệ. Vui lòng nhập từ 1-5!") 