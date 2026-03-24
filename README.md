# ROS2 Robot Challenge - Avtonomni mobilni roboti (AMR)

Dobrodošli na robotskem izzivu! Ta repozitorij vsebuje začetno programsko kodo za upravljanje mobilnih robotov s sistemom ROS2.
Trenutno vsebuje preprosto vozlišče (`drive_straight`), ki na 100ms pošilja ukaze za premikanje robota naravnost naprej.

## Viri in dokumentacija

Preden začnete, si obvezno preberite podrobna navodila izziva:
*  **[Glavna navodila izziva (Google Doc)](https://docs.google.com/document/d/12gec_yjAopAPG4-TW27NjqRAmlWTLbvkk2c-xxmtCVM/edit?tab=t.0)**
*  **Ubiquity Robotics dokumentacija:** [learn2.ubiquityrobotics.com](https://learn2.ubiquityrobotics.com/jazzy/)
*  **ROS2 dokumentacija:** [docs.ros.org](https://docs.ros.org)

## Povezovanje z robotom
Za izvajanje kode na robotu se morate nanj povezati prek SSH. Odprite terminal ali Powershell in vpišite:

```bash
ssh ubuntu@<ip_naslov_robota>
```

*(Za točen IP naslov robota preverite tablo, privzeto geslo je "ubuntu")*

## Ročno krmiljenje (Teleop)

Ko se na robota povežete in še preden se začnete ukvarjati z avtonomno kodo, preverite, ali je robot sploh *živ*. Za ročno upravljanje robota prek tipkovnice uporabite:

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

*Navodila za upravljanje se izpišejo v terminalu (vozimo s tipkami `u`, `i`, `o`, `j`, `k`, `l`, `m`, `,`, `.`).*


## Uporaba ROS2 paketa na robotu

Ko ste uspešno povezani z robotom in ga lahko upravljate s tipkovnico, sledite naslednjim korakom za pripravo delovnega okolja:

1. **Pojdite v delovni prostor ROS2 (ROS2 workspace):**
   Delovni prostor se običajno nahaja v `~/ros2_challenge_ws`. Če še ne obstaja, ga prosim ustvarite:
   ```bash
   cd ~/ros2_challenge_ws
   ```

2. **Klonirajte repozitorij:**
   V poddirektorij `src` klonirajte ta Github repozitorij:
   ```bash
   cd src
   git clone https://github.com/UbiquityRobotics/ur_robot_challenge.git
   ```

3. **Prevedite paket (Build):**
   Premaknite se nazaj v koren delovnega prostora in zaženite gradnjo paketa z uporabo `colcon`:
   ```bash
   cd ~/ros2_challenge_ws 
   colcon build --packages-select ur_robot_challenge
   ```

4. **Naložite okolje:**
   Da bo sistem ROS2 prepoznal vaš na novo preveden paket, morate vedno "sourcati" okolje:
   ```bash
   source install/setup.bash
   ```

## Zagon vozlišča na robotu

Ko je okolje naloženo, lahko zaženete vozlišče, ki bo robota peljalo naravnost. Zagotovite, da je robot na varnem in ima prosto pot brez ovir!

```bash
ros2 run ur_robot_challenge drive_straight
```

Robot bi se moral začeti premikati naravnost takoj po izvedbi zgornjega ukaza. Za ustavitev pritisnite `Ctrl+C` v terminalu.

## Struktura paketa

* `ur_robot_challenge/drive_straight.py`: Python izvorna koda vozlišča. Naroča se in objavlja `Twist` sporočila na temi `/cmd_vel`.
* `package.xml` & `setup.py`: Konfiguracijske datoteke ROS2 paketa.


## Preverjanje kamere (za 3. in 4. podiziv)

Za zahtevnejše dele izziva boste potrebovali dostop do kamere. Da preverite, pod katero temo (topic) robot oddaja sliko, uporabite ukaz:

```bash
ros2 topic list | grep camera
```

V vašem programu se boste morali naročiti (subscribe) na to temo (običajno `/camera/image_raw` ali podobno), da bo robot lahko "videl" okolico in zaznaval osebe.
