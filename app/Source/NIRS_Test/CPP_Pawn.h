// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Pawn.h"
#include "CPP_Pawn.generated.h"

UCLASS()
class NIRS_TEST_API ACPP_Pawn : public APawn
{
	GENERATED_BODY()

public:
	// Sets default values for this pawn's properties
	ACPP_Pawn();

protected:
	// Called when the game starts or when spawned
	virtual void BeginPlay() override;

	//
	int radiationMap[7][7][7];

public:	
	// Called every frame
	virtual void Tick(float DeltaTime) override;

	// Called to bind functionality to input
	virtual void SetupPlayerInputComponent(class UInputComponent* PlayerInputComponent) override;

	//
	UFUNCTION(BlueprintCallable)
		int getFuflo(int x, int y, int z);



};
