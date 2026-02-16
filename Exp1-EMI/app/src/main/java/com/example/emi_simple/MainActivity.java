package com.example.emi_simple;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    EditText etPrincipal, etRate, etTime;
    Button btnCalculate;
    TextView tvResult;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        etPrincipal = findViewById(R.id.etPrincipal);
        etRate = findViewById(R.id.etRate);
        etTime = findViewById(R.id.etTime);
        btnCalculate = findViewById(R.id.btnCalculate);
        tvResult = findViewById(R.id.tvResult);

        btnCalculate.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                String principalStr = etPrincipal.getText().toString();
                String rateStr = etRate.getText().toString();
                String timeStr = etTime.getText().toString();

                if (principalStr.isEmpty() || rateStr.isEmpty() || timeStr.isEmpty()) {
                    tvResult.setText("Please enter all values");
                    return;
                }

                double P = Double.parseDouble(principalStr);
                double annualRate = Double.parseDouble(rateStr);
                int years = Integer.parseInt(timeStr);

                double R = annualRate / (12 * 100);
                int N = years * 12;

                double EMI = (P * R * Math.pow(1 + R, N)) /
                        (Math.pow(1 + R, N) - 1);

                tvResult.setText("Monthly EMI = ₹ " + String.format("%.2f", EMI));
            }
        });
    }
}
