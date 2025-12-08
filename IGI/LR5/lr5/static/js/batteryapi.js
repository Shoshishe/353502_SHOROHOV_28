const details = document.getElementById("battery-info");
const isCharging = document.createElement('p');
const chargeInfo = document.createElement('p');
const dischargeInfo = document.createElement('p');

details.appendChild(isCharging);
details.appendChild(chargeInfo);
details.appendChild(dischargeInfo);

navigator.getBattery().then((battery) => {
    function updateAllBatteryInfo() {
        updateChargeInfo();
        updateLevelInfo();
        updateChargingInfo();
        updateDischargingInfo();
    }
    updateAllBatteryInfo();

    battery.addEventListener("chargingchange", () => {
        updateChargeInfo();
    });
    function updateChargeInfo() {
        isCharging.innerHTML = battery.charging ? "Charging" : "Not charging";
    }

    battery.addEventListener("levelchange", () => {
        updateLevelInfo();
    });
    function updateLevelInfo() {
        details.firstChild.nodeValue = (`Battery level: ${battery.level * 100}%`);
    }

    battery.addEventListener("chargingtimechange", () => {
        updateChargingInfo();
    });
    function updateChargingInfo() {
        chargeInfo.innerHTML = `Battery charging time: ${battery.chargingTime} seconds`;
    }

    battery.addEventListener("dischargingtimechange", () => {
        updateDischargingInfo();
    });
    function updateDischargingInfo() {
        dischargeInfo.innerHTML = `Battery discharging time: ${battery.dischargingTime} seconds`;
    }
});