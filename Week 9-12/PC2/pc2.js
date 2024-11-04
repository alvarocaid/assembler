var LED_A = 2;
var LED_B = 3;
var LED_C = 4;
var LED_D = 5;

function leds_to(L_or_H) {
    digitalWrite(LED_A, L_or_H);
    digitalWrite(LED_B, L_or_H);
    digitalWrite(LED_C, L_or_H);
    digitalWrite(LED_D, L_or_H);
}

function setup(){
    pinMode(LED_A, OUTPUT);
    pinMode(LED_B, OUTPUT);
    pinMode(LED_C, OUTPUT);
    pinMode(LED_D, OUTPUT);

    leds_to(LOW);
}

function runCycle() {
    // Estado 1
    leds_to(LOW);
    delay(2000);
    
    // Estado 2
    digitalWrite(LED_A, HIGH);
    delay(4000);
    digitalWrite(LED_A, LOW);

    // Estado 3
    digitalWrite(LED_A, HIGH);
    digitalWrite(LED_B, HIGH);
    delay(2000);
    digitalWrite(LED_A, LOW);
    digitalWrite(LED_B, LOW);

    // Estado 4
    digitalWrite(LED_C, HIGH);
    delay(5000);
    digitalWrite(LED_C, LOW);

    // Estado 5
    digitalWrite(LED_C, HIGH);
    digitalWrite(LED_D, HIGH);
    delay(3000);
    digitalWrite(LED_C, LOW);
    digitalWrite(LED_D, LOW);

    // Estado 6
    leds_to(HIGH);
    delay(2000);
    leds_to(LOW);
}

function blinkAllLeds(times) {
    for (var i = 0; i < times; i++) {
        leds_to(LOW); // Se apagan los leds por un segundo
        delay(1000);
        leds_to(HIGH); // Se prenden los leds por un segundo
        delay(1000);
    }
}

function main() {
    for (var i = 0; i < 4; i++) { // Se ejecuta 4 veces el ciclo
        runCycle();
    }

    blinkAllLeds(2); // Luego de los 4 ciclos se procede al parpadeo

    // Quedan prendidos indefinidamente
}

main();
