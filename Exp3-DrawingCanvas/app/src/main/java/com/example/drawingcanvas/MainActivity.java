package com.example.drawingcanvas;

import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        DrawingView drawingView = new DrawingView(this);
        setContentView(drawingView);
    }
}
