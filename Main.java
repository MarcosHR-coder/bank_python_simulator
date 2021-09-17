import javax.swing.*;

public class Main extends JFrame {

  private final int HEIGHT = 500;
  private final int WIDTH = 700;

  private JLabel personalData, sald, calculates;
  private JLabel currentSald, saveSald, CDTsald, total;
  private JButton requestChange, resetValues;
  private JLabel inputCurrent, inputSaveAcc, inputSaveCDT, inputTotal;

  private Main() {

    setLayout(null);
    setSize(WIDTH, HEIGHT);
    setLocationRelativeTo(null);
    setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    setVisible(true);
    setTitle("Peac Inc Bank Management");
    setResizable(false);

    this.configureLabelComponents();

  }

  private void configureLabelComponents () {

    sald = new JLabel("Saldo");
    sald.setSize(200, 15);
    sald.setLocation(30, 20);
    add(sald);

    currentSald = new JLabel("Saldo Corriente: ");
    currentSald.setSize(200, 15);
    currentSald.setLocation(100, 100);
    add(currentSald);

    inputCurrent = new JLabel("50.00");
    inputCurrent.setSize(200, 15);
    inputCurrent.setLocation(220, 100);
    add(inputCurrent);

    saveSald = new JLabel("Saldo Ahorros: ");
    saveSald.setSize(200, 15);
    saveSald.setLocation(100, 165);
    add(saveSald);

    inputSaveAcc = new JLabel("50.00");
    inputSaveAcc.setSize(200, 15);
    inputSaveAcc.setLocation(220, 165);
    add(inputSaveAcc);


    calculates = new JLabel("Cálculos");
    calculates.setSize(300, 15);
    calculates.setLocation(30, 230);
    add(calculates);

  }

  public static void main(String[] args) {
    new Main();
  }
}