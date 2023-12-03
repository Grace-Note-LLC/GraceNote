#define DATA_BUTTON   3
#define DECODER_A     8
#define DECODER_B     7
#define DECODER_C     11
#define DECODER_D     10

int count = 0;

void setup() {
  pinMode(DATA_BUTTON, INPUT);
  attachInterrupt(DATA_BUTTON, isr_data_button_falling, FALLING);

  pinMode(DECODER_A, OUTPUT);
  pinMode(DECODER_B, OUTPUT);
  pinMode(DECODER_C, OUTPUT);
  pinMode(DECODER_D, OUTPUT);
    
  Serial.begin(9600);

  disp(count);
}

void loop() {
  Serial.println(count);
}

void disp(int num)
{
  switch(num)
  {
    case 0:
      seven_seg(0, 0, 0, 0);
      return;
    case 1:
      seven_seg(0, 0, 0, 1);
      return;
    case 2: 
      seven_seg(0, 0, 1, 0);
      return;
    case 3:
      seven_seg(0, 0, 1, 1);
      return;
    case 4: 
      seven_seg(0, 1, 0, 0);
      return;
    case 5:
      seven_seg(0, 1, 0, 1);
      return;
    case 6:
      seven_seg(0, 1, 1, 0);
      return;
    case 7:
      seven_seg(0, 1, 1, 1);
      return;
    case 8:
      seven_seg(1, 0, 0, 0);
      return;
    case 9:
      seven_seg(1, 0, 0, 1);
      return;
    default:
      seven_seg(0, 0, 0, 0);
      return;
  }
}

void seven_seg(bool D, bool C, bool B, bool A)
{
  digitalWrite(DECODER_A, A);
  digitalWrite(DECODER_B, B);
  digitalWrite(DECODER_C, C);
  digitalWrite(DECODER_D, D);
}

void isr_data_button_falling()
{
  count++;
  if(count>9)
  {
    count = 0;
  }
  disp(count);
//  Serial.println(count);
//  delay(3000);
}
