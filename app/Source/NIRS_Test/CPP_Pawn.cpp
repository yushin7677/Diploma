// Fill out your copyright notice in the Description page of Project Settings.


#include "CPP_Pawn.h"

// Sets default values
ACPP_Pawn::ACPP_Pawn()
{
 	// Set this pawn to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;

	int radiationMap2[7][7][7] = { {
		{112, 109, 102, 66, 0, 0, 0},
		{ 112, 111, 110, 93, 0, 0, 0 },
		{ 110, 108, 100, 66, 0, 0, 0 },
		{ 108, 104, 92, 53, 0, 0, 0 },
		{ 105, 102, 90, 56, 0, 0, 0 },
		{ 103, 99, 83, 40, 0, 0, 0 },
		{ 102, 98, 81, 39, 0, 0, 0 }
		},
	{
	{115, 115, 121, 104, 0, 0, 0},
	{116, 120, 146, 268, 0, 0, 0},
	{114, 115, 121, 118, 0, 0, 0},
	{111, 110, 108, 80, 0, 0, 0},
	{108, 108, 109, 120, 0, 0, 0},
	{106, 104, 93, 43, 0, 0, 0},
	{105, 102, 91, 49, 0, 0, 0}
	},
	{
	{117, 112, 104, 72, 0, 0, 0},
	{117, 114, 113, 99, 0, 0, 0},
	{117, 113, 108, 84, 0, 0, 0},
	{115, 110, 101, 72, 0, 0, 0},
	{112, 107, 96, 66, 0, 0, 0},
	{110, 104, 88, 49, 0, 0, 0},
	{109, 103, 86, 48, 0, 0, 0}
	},
	{
	{123, 115, 101, 73, 0, 0, 0},
	{124, 117, 107, 86, 0, 0, 0},
	{124, 119, 115, 131, 0, 0, 0},
	{123, 117, 111, 121, 0, 0, 0},
	{120, 113, 100, 75, 0, 0, 0},
	{118, 110, 92, 52, 0, 0, 0},
	{117, 109, 91, 61, 0, 0, 0}
	},
	{
	{136, 129, 114, 79, 0, 0, 0},
	{138, 132, 119, 84, 0, 0, 0},
	{139, 135, 129, 104, 0, 0, 0},
	{138, 134, 125, 96, 0, 0, 0},
	{136, 130, 117, 83, 0, 0, 0},
	{133, 127, 112, 75, 0, 0, 0},
	{132, 126, 110, 75, 0, 0, 0}
	},
	{
	{155, 156, 154, 131, 0, 0, 0},
	{158, 160, 161, 134, 0, 0, 0},
	{161, 169, 189, 209, 0, 0, 0},
	{160, 166, 176, 168, 0, 0, 0},
	{157, 160, 163, 146, 0, 0, 0},
	{154, 157, 157, 138, 0, 0, 0},
	{152, 155, 155, 137, 0, 0, 0}
	},
	{
	{170, 182, 201, 236, 0, 0, 0},
	{174, 188, 208, 171, 0, 0, 0},
	{180, 207, 299, 642, 0, 0, 0},
	{178, 199, 250, 346, 0, 0, 0},
	{174, 190, 223, 279, 0, 0, 0},
	{170, 185, 212, 264, 0, 0, 0},
	{168, 183, 209, 260, 0, 0, 0}
	}
	};

	for (int i = 0; i < 7; i++)
		for (int j = 0; j < 7; j++)
			for (int k = 0; k < 7; k++)
				this->radiationMap[i][j][k] = radiationMap2[i][j][k];

}

// Called when the game starts or when spawned
void ACPP_Pawn::BeginPlay()
{
	Super::BeginPlay();
	
}

// Called every frame
void ACPP_Pawn::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);

}

// Called to bind functionality to input
void ACPP_Pawn::SetupPlayerInputComponent(UInputComponent* PlayerInputComponent)
{
	Super::SetupPlayerInputComponent(PlayerInputComponent);

}

int ACPP_Pawn::getFuflo(int x, int y, int z) {

	int fuflo = 0; 
	if (x > -450 && y > -450 && z > -450 && x < 450 && y < 450 && z < 450) {
		int i = (x + 450) / 150, j = (y + 450) / 150, k = (z + 450) / 150;
		int x1 = i * 150 - 450, y1 = j * 150 - 450, z1 = k * 150 - 450;
		int x2 = x1 + 150, y2 = y1 + 150, z2 = z1 + 150;
		fuflo = radiationMap[i][j][k] * (x2 - x) / 150 * (y2 - y) / 150 * (z2 - z) / 150 +
			radiationMap[i + 1][j][k] * (x - x1) / 150 * (y2 - y) / 150 * (z2 - z) / 150 +
			radiationMap[i][j + 1][k] * (x2 - x) / 150 * (y - y1) / 150 * (z2 - z) / 150 +
			radiationMap[i][j][k + 1] * (x2 - x) / 150 * (y2 - y) / 150 * (z - z1) / 150 +
			radiationMap[i][j + 1][k + 1] * (x2 - x) / 150 * (y - y1) / 150 * (z - z1) / 150 +
			radiationMap[i + 1][j][k + 1] * (x - x1) / 150 * (y2 - y) / 150 * (z - z1) / 150 +
			radiationMap[i + 1][j + 1][k] * (x - x1) / 150 * (y - y1) / 150 * (z2 - z) / 150 +
			radiationMap[i + 1][j + 1][k + 1] * (x - x1) / 150 * (y - y1) / 150 * (z - z1) / 150;
	}
	else fuflo = 0;
	return fuflo;

}

